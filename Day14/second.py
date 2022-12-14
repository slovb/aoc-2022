start = (500, 0)


def debug(rocks, sand, bounds):
    minX, maxX, minY, maxY = bounds
    rows = []
    for j in range(minY, maxY + 2):
        row = []
        for i in range(minX-2, maxX + 3):
            if (i, j) in sand:
                row.append('O')
            elif (i, j) in rocks:
                row.append('#')
            elif (i, j) == start:
                row.append('+')
            else:
                row.append(' ')
        rows.append(''.join(row))
    rows.append('#'*len(rows[0]))
    print('\n'.join(rows))


def down(p):
    x, y = p
    return (x, y+1)


def down_left(p):
    x, y = p
    return (x-1, y+1)


def down_right(p):
    x, y = p
    return (x+1, y+1)


def solve(rocks, bounds):
    minX, maxX, minY, maxY = bounds
    sand = set()

    def oob(p):
        _, y = p
        if y > maxY:
            return True
        return False

    def occupied(p):
        return p in rocks or p in sand

    p = start
    old = []
    while True:
        if oob(p):
            minX = min(minX, p[0])
            maxX = max(maxX, p[0])
            sand.add(p)
            if len(old) == 0:
                break
            p = old.pop()
        elif not occupied(down(p)):
            old.append(p)
            p = down(p)
        elif not occupied(down_left(p)):
            old.append(p)
            p = down_left(p)
        elif not occupied(down_right(p)):
            old.append(p)
            p = down_right(p)
        else:
            sand.add(p)
            if len(old) == 0:
                break
            p = old.pop()
    
    debug(rocks, sand, (minX, maxX, minY, maxY))
    return len(sand)


def between(a, b):
    x, y = a
    u, v = b
    points = []
    for i in range(min(x, u) + 1, max(x, u)):
        points.append((i, y))
    for j in range(min(y, v) + 1, max(y, v)):
        points.append((x, j))
    return points


def read_part(part):
    a, b = part.split(',')
    return (int(a), int(b))


def read(path):
    rocks = set()
    minX = start[0]
    maxX = start[0]
    minY = start[1]
    maxY = start[1]
    with open(path, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()]
        for row in rows:
            parts = map(read_part, row.split(" -> "))
            left = next(parts)
            for right in parts:
                rocks.add(left)
                minX = min(left[0], minX)
                maxX = max(left[0], maxX)
                minY = min(left[1], minY)
                maxY = max(left[1], maxY)
                b = between(left, right)
                for p in b:
                    rocks.add(p)
                left = right
            rocks.add(left)
            minX = min(left[0], minX)
            maxX = max(left[0], maxX)
            minY = min(left[1], minY)
            maxY = max(left[1], maxY)
    # maxY += 1  # another row
    return rocks, (minX, maxX, minY, maxY)


def main(path):
    rocks, bounds = read(path)
    return solve(rocks, bounds)


def display(output):
    print('\n')
    try:
        iterator = iter(output)
    except TypeError:
        print(output)
        pass
    else:
        for line in iterator:
            print(line)


if __name__ == "__main__":
    import os
    dirname = os.path.realpath(os.path.dirname(__file__))
    filename = 'input.txt' if True else 'test.txt'
    path = f'{dirname}/{filename}'
    import sys

    if (len(sys.argv) < 2):
        display(main(path))
    else:
        for f in sys.argv[1:]:
            display(main(f))
