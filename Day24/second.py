import math
# 2677 too high
# 2077 too high

def solve(data):
    width, height, depth, blizzards = data

    def is_oob(pos):
        x, y, _ = pos
        if x < 0 or x >= width:
            return True
        if (x, y) == (0, -1) or (x, y) == (width - 1, height):
            return False
        return y < 0 or y >= height

    def at_goal(pos, checkpoints):
        x, y, _ = pos
        return x == width - 1 and y == height and checkpoints == 2

    def at_checkpoint1(pos, checkpoints):
        return checkpoints == 0 and at_goal(pos, 2)
    
    def at_checkpoint2(pos, checkpoints):
        x, y, _ = pos
        return checkpoints == 1 and x == 0 and y == -1

    def distance(pos, checkpoints):  # probably has some off by one, but ended up working before debugging
        x, y, _ = pos
        cross = (width - 1) + height
        if checkpoints == 0:
            return abs(width - 1 - x) + abs(height - y) + 2 * cross
        elif checkpoints == 1:
            return x + y + 1 + cross
        return abs(width - 1 - x) + abs(height - y)

    blockers = set()
    for b in blizzards:
        for t in range(depth):
            blockers.add(b(t))

    visited = {}
    queue = [((0, -1, 0), 0, 0)]  # (x y d) t
    best = width * height * depth * 3
    while len(queue) > 0:
        pos, checkpoints, time = queue.pop()
        if distance(pos, checkpoints) + time >= best:
            continue
        x, y, d = pos
        if checkpoints % 2 == 0:  # priority ordering to skip implementing heap
            neighbors = [
                (x, y, (d + 1) % depth),
                (x - 1, y, (d + 1) % depth),
                (x, y - 1, (d + 1) % depth),
                (x + 1, y, (d + 1) % depth),
                (x, y + 1, (d + 1) % depth),
            ]
        else:
            neighbors = [
                (x, y, (d + 1) % depth),
                (x + 1, y, (d + 1) % depth),
                (x, y + 1, (d + 1) % depth),
                (x - 1, y, (d + 1) % depth),
                (x, y - 1, (d + 1) % depth),
            ]
        for neighbor in neighbors:
            if is_oob(neighbor):
                continue
            if neighbor in blockers:
                continue
            nc = checkpoints
            if at_checkpoint1(neighbor, checkpoints):
                nc = 1
            elif at_checkpoint2(neighbor, checkpoints):
                nc = 2
            key = neighbor + (nc,)
            if key in visited:
                if visited[key] <= (time + 1):
                    continue
            visited[key] = time + 1
            if at_goal(neighbor, nc):
                if time + 1 < best:
                    best = time + 1
                    print(best)
            else:
                queue.append((neighbor, nc, time + 1))
    return best


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
