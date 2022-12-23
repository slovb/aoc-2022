def score(elves):
    minX, minY, maxX, maxY = bounds(elves)
    return (1 + maxX - minX) * (1 + maxY - minY) - len(elves)


def bounds(elves):
    minX = None
    minY = None
    maxX = None
    maxY = None
    for p in elves:
        x, y = p
        if minX is None:
            minX, maxX, minY, maxY = x, x, y, y
        minX = min(minX, x)
        minY = min(minY, y)
        maxX = max(maxX, x)
        maxY = max(maxY, y)
    return (minX, minY, maxX, maxY)


def debug(elves):
    minX, minY, maxX, maxY = bounds(elves)
    rows = []
    for y in range(minY, maxY + 1):
        row = []
        for x in range(minX, maxX + 1):
            if (x, y) in elves:
                row.append('#')
            else:
                row.append('.')
        rows.append(''.join(row))
    return '\n'.join(rows) + '\n'


def update(elves, i):
    step = {
        'NW':   lambda x, y: (x - 1,    y - 1),
        'N':    lambda x, y: (x,        y - 1),
        'NE':   lambda x, y: (x + 1,    y - 1),
        'W':    lambda x, y: (x - 1,    y),
        'E':    lambda x, y: (x + 1,    y),
        'SW':   lambda x, y: (x - 1,    y + 1),
        'S':    lambda x, y: (x,        y + 1),
        'SE':   lambda x, y: (x + 1,    y + 1),
    }

    moves = {}
    for origin in elves:
        x, y = origin
        neighbors = {d: step[d](x, y) not in elves for d in step}
        if all(neighbors.values()):
            plan = origin
        else:
            propositions = [
                (all(neighbors[d] for d in ['N', 'NW', 'NE']), 'N'),
                (all(neighbors[d] for d in ['S', 'SE', 'SW']), 'S'),
                (all(neighbors[d] for d in ['W', 'NW', 'SW']), 'W'),
                (all(neighbors[d] for d in ['E', 'NE', 'SE']), 'E'),
            ]
            plan = origin
            for k in range(4):
                condition, direction = propositions[(i + k) % 4]
                if condition:
                    plan = step[direction](x, y)
                    break
        moves[origin] = plan
    invalid = True
    while invalid:
        count = {}
        invalid = False
        for move in moves.values():
            if move not in count:
                count[move] = 1
            else:
                count[move] += 1
                invalid = True
        for origin, move in moves.items():
            if count[move] > 1:
                moves[origin] = origin
    output = set(moves.values())
    return output


def solve(elves):
    print(debug(elves))
    for i in range(10):
        elves = update(elves, i)
        print(debug(elves))
    return score(elves)


def read(path):
    elves = set()
    with open(path, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()]
        for j, row in enumerate(rows):
            for i, c in enumerate(row):
                if c == '#':
                    elves.add((i, j))
        return elves


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
