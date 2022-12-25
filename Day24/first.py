import math


def solve(data):
    width, height, depth, blizzards = data

    def is_oob(pos):
        x, y, _ = pos
        return x < 0 or x >= width or y < 0 or y >= height

    def at_goal(pos):
        x, y, _ = pos
        return x == width - 1 and y == height - 1

    def distance(pos):
        x, y, _ = pos
        return abs(width - 1 - x) + abs(height - 1 - y)

    blockers = set()
    for b in blizzards:
        for t in range(depth):
            blockers.add(b(t))

    visited = {}
    queue = [((0, -1, d), d) for d in range(depth)]  # (x y d) t
    best = width * height * depth
    while len(queue) > 0:
        pos, time = queue.pop()
        if distance(pos) + time >= best:
            continue
        x, y, d = pos
        neighbors = [
            (x, y, (d + 1) % depth),
            (x - 1, y, (d + 1) % depth),
            (x, y - 1, (d + 1) % depth),
            (x + 1, y, (d + 1) % depth),
            (x, y + 1, (d + 1) % depth),
        ]
        for neighbor in neighbors:
            if is_oob(neighbor):
                continue
            if neighbor in blockers:
                continue
            if neighbor in visited:
                if visited[neighbor] <= (time + 1):
                    continue
            visited[neighbor] = time + 1
            if at_goal(neighbor):
                if time + 1 < best:
                    best = time + 1
                    print(best)
            else:
                queue.append((neighbor, time + 1))
    return best + 1


def read(path):
    with open(path, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()]
        width = len(rows[0]) - 2
        height = len(rows) - 2
        depth = math.lcm(width, height)

        def right(x, y):
            return lambda t: ((x + t) % width, y, t % depth)

        def down(x, y):
            return lambda t: (x, (y + t) % height, t % depth)

        def left(x, y):
            return lambda t: ((x - t) % width, y, t % depth)

        def up(x, y):
            return lambda t: (x, (y - t) % height, t % depth)
        
        blizzards = []
        for y, row in enumerate(rows[1:-1]):
            for x, c in enumerate(row[1:-1]):
                if c == '>':
                    blizzards.append(right(x, y))
                elif c == 'v':
                    blizzards.append(down(x, y))
                elif c == '<':
                    blizzards.append(left(x, y))
                elif c == '^':
                    blizzards.append(up(x, y))
     
        return (width, height, depth, blizzards)


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
