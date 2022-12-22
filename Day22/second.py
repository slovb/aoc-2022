step = [
    lambda p: (p[0] + 1, p[1]),
    lambda p: (p[0], p[1] + 1),
    lambda p: (p[0] - 1, p[1]),
    lambda p: (p[0], p[1] - 1),
]


def score(pos, facing):
    x, y = pos
    return 1000 * (y + 1) + 4 * (x + 1) + facing


def solve(data):
    spaces, walls, _, _, movement, pos = data
    facing = 0
    left_is_right = False
    while len(movement) > 0:
        move = movement.pop(0)
        print(f'move {move} from {pos} {facing}')
        if (not left_is_right and move == 'L') or (left_is_right and move == 'R'):
            facing = (facing - 1) % 4
        elif move in ['L', 'R']:
            facing = (facing + 1) % 4
        else:
            for _ in range(move):
                candidate = step[facing](pos)
                if candidate in walls:
                    break
                elif candidate in spaces:
                    pos = candidate
                else:
                    x, y = pos  # important change
                    new_facing = facing
                    new_left_is_right = left_is_right
                    print(pos, facing, left_is_right)
                    if facing == 0:
                        if y < 50:
                            candidate = (99,                149 - (y % 50))
                            new_facing = 2
                        elif y < 100:
                            candidate = (100 + (y % 50),    49)
                            new_facing = 3
                        elif y < 150:
                            candidate = (149,               49 - (y % 50))
                            new_facing = 2
                        else:
                            candidate = (50 + (y % 50),     149)
                            new_facing = 3
                    elif facing == 1:
                        if x < 50:
                            candidate = (100 + (x % 50),    0)
                            # new_left_is_right = not new_left_is_right
                        elif x < 100:
                            candidate = (49,                150 + (x % 50))
                            new_facing = 2
                        else:
                            candidate = (99,                50 + (x % 50))
                            new_facing = 2
                    elif facing == 2:
                        if y < 50:
                            candidate = (0,                 149 - (y % 50))
                            new_facing = 0
                            # new_left_is_right = not new_left_is_right
                        elif y < 100:
                            candidate = (0 + (y % 50),      100)
                            new_facing = 1
                        elif y < 150:
                            candidate = (50,                49 - (y % 50))
                            new_facing = 0
                            # new_left_is_right = not new_left_is_right
                        else:
                            candidate = (50 + (y % 50),     0)
                            new_facing = 1
                    else:
                        if x < 50:
                            candidate = (50,                50 + (x % 50))
                            new_facing = 0
                        elif x < 100:
                            candidate = (0,                 150 + (x % 50))
                            new_facing = 0
                        else:
                            candidate = (0 + (x % 50),      199)
                            # new_left_is_right = not new_left_is_right
                    if candidate in walls:
                        break
                    if candidate not in spaces:
                        raise Exception(candidate)
                    pos = candidate
                    facing = new_facing
                    left_is_right = new_left_is_right
                    print(pos, facing, left_is_right)
                # print(pos)
        # print(f'arrive {pos} {direction}')
    return score(pos, facing)


def parse_movement(line: str):
    data = []
    j = 0
    for i in range(len(line)):
        if line[i].isdigit():
            continue
        data.append(int(line[j:i]))
        data.append(line[i])
        j = i + 1
    data.append(int(line[j:]))
    return data


def read(path):
    spaces = set()
    walls = set()
    movement = []
    with open(path, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()]
        heights = [0] * max([len(row) for row in rows[:-2]])
        widths = [0] * (len(rows) - 2)
        movement = parse_movement(rows[-1])
        start = None
        for y, row in enumerate(rows[:-2]):
            for x, c in enumerate(row):
                if c == ' ':
                    continue
                heights[x] += 1
                widths[y] += 1
                if c == '#':
                    walls.add((x, y))
                else:
                    spaces.add((x, y))
                    if start is None:
                        start = (x, y)
        return (spaces, walls, heights, widths, movement, start)


def main(path, is_test):
    if is_test:
        raise Exception('hardcoding mappings')
    data = read(path)
    return solve(data)


def display(output):
    print('\n')
    print(output)


if __name__ == "__main__":
    is_test = False
    import os
    dirname = os.path.realpath(os.path.dirname(__file__))
    filename = 'test.txt' if is_test else 'input.txt'
    path = f'{dirname}/{filename}'
    import sys

    if (len(sys.argv) < 2):
        display(main(path, is_test=is_test))
    else:
        for f in sys.argv[1:]:
            display(main(f))
