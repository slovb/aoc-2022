step = [
    lambda p: (p[0] + 1, p[1]),
    lambda p: (p[0], p[1] + 1),
    lambda p: (p[0] - 1, p[1]),
    lambda p: (p[0], p[1] - 1),
]

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3


def score(pos, facing):
    x, y = pos
    return 1000 * (y + 1) + 4 * (x + 1) + facing


def solve(data):
    spaces, walls, _, _, movement, pos = data
    facing = 0
    side = 50
    while len(movement) > 0:
        move = movement.pop(0)
        print(f'move {move} from {pos} {facing}')
        if move == 'L':
            facing = (facing - 1) % 4
        elif move == 'R':
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
                    if facing == RIGHT:
                        if y // side == 0:
                            candidate = (2*side - 1,            3 * side - 1 - (y % side))
                            new_facing = LEFT
                        elif y // side == 1:
                            candidate = (2*side + (y % side),   side - 1)
                            new_facing = UP
                        elif y // side == 2:
                            candidate = (3*side - 1,            side - 1 - (y % side))
                            new_facing = LEFT
                        else:
                            candidate = (side + (y % side),     3*side - 1)
                            new_facing = UP
                    elif facing == DOWN:
                        if x // side == 0:
                            candidate = (2*side + (x % side),   0)
                        elif x // side == 1:
                            candidate = (side - 1,              3*side + (x % side))
                            new_facing = LEFT
                        else:
                            candidate = (2*side - 1,            side + (x % side))
                            new_facing = LEFT
                    elif facing == LEFT:
                        if y // side == 0:
                            candidate = (0,                     3*side - 1 - (y % side))
                            new_facing = RIGHT
                        elif y // side == 1:
                            candidate = (0 + (y % side),        2*side)
                            new_facing = DOWN
                        elif y // side == 2:
                            candidate = (side,                  side - 1 - (y % side))
                            new_facing = RIGHT
                        else:
                            candidate = (side + (y % side),     0)
                            new_facing = DOWN
                    else:
                        if x // side == 0:
                            candidate = (side,                  side + (x % side))
                            new_facing = RIGHT
                        elif x // side == 1:
                            candidate = (0,                     3*side + (x % side))
                            new_facing = RIGHT
                        else:
                            candidate = (0 + (x % side),        4*side - 1)
                            # unchanged
                    if candidate in walls:
                        break
                    if candidate not in spaces:
                        raise Exception(candidate)
                    pos = candidate
                    facing = new_facing
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
