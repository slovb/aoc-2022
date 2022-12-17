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


class State():
    def __init__(self):
        self.index = 0
        self.top = -1
        self.pos = (2, 4 + self.top)
        self.blocks = set()
        self.fallen_rocks = 0
        self.bottom = 0

    def step(self, direction):
        if direction == '<':
            new_pos = left(self.pos)
        else:
            new_pos = right(self.pos)
        shape = shape_at(self.index, new_pos)
        if is_ok(shape, self.blocks):
            self.pos = new_pos

        new_pos = down(self.pos)
        shape = shape_at(self.index, new_pos)
        if is_ok(shape, self.blocks):
            self.pos = new_pos
        else:
            shape = shape_at(self.index, self.pos)
            for p in shape:
                self.top = max(self.top, p[1])
                self.blocks.add(p)
            self.pos = (2, 4 + self.top)
            self.index += 1
            self.fallen_rocks += 1


def solve(data):
    state = State()
    target = 1000000000000

    # d = 0
    # while fallen_rocks < 1000000000000:
    #     direction = data[d % len(data)]
    #     d += 1
    #     if (d % len(data) == 0):
    #         print(debug())
    #         print(' ')
    for direction in data:
        state.step(direction)
    base_top = state.top
    base_fallen = state.fallen_rocks

    for direction in data:
        state.step(direction)
    diff_top = state.top - base_top
    diff_fallen = state.fallen_rocks - base_fallen

    times = (target - state.fallen_rocks) // diff_fallen
    padding_top = times * diff_top
    padding_fallen = times * diff_fallen

    for direction in data:
        state.step(direction)
        if state.fallen_rocks + padding_fallen == target + 1:
            break

    return state.top + padding_top


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
