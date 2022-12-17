width = 7

shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
]


def shape_at(index, pos):  # pos is bottom left
    shape = shapes[index % len(shapes)]
    x, y = pos
    output = []
    for p in shape:
        u, v = p
        output.append((x+u, y+v))
    return output


def down(pos):
    x, y = pos
    return (x, y - 1)


def left(pos):
    x, y = pos
    return (x - 1, y)


def right(pos):
    x, y = pos
    return (x + 1, y)


def is_ok(shape, blocks):
    for p in shape:
        x, y = p
        if y < 0 or x < 0 or x >= width:
            return False
        if p in blocks:
            return False
    return True


def solve(data):
    index = 0
    top = -1
    pos = (2, 4 + top)
    blocks = set()
    fallen_rocks = 0

    def debug():
        shape = shape_at(index, pos)
        rows = []
        for y in range(top + 7, -1, -1):
            row = []
            for x in range(width):
                if (x, y) in blocks:
                    row.append('#')
                elif (x, y) in shape:
                    row.append('@')
                else:
                    row.append('.')
            rows.append(''.join(row))
        return '\n'.join(rows)

    d = 0
    while fallen_rocks < 2023:
        direction = data[d % len(data)]
        d += 1
        if direction == '<':
            new_pos = left(pos)
        else:
            new_pos = right(pos)
        shape = shape_at(index, new_pos)
        if is_ok(shape, blocks):
            pos = new_pos
        # print(f'================= {pos} ===========')
        # print(debug())
        # print(' ')

        new_pos = down(pos)
        shape = shape_at(index, new_pos)
        if is_ok(shape, blocks):
            pos = new_pos
        else:
            shape = shape_at(index, pos)
            for p in shape:
                top = max(top, p[1])
                blocks.add(p)
            pos = (2, 4 + top)
            index += 1
            fallen_rocks += 1
        # print(debug())
        # print(' ')

    return top - 1


def read(path):
    with open(path, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()]
    return rows[0]


def main(path, is_test):
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
