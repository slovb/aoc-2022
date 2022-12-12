from heapq import heappop, heappush


def alternatives(p):
    x, y = p
    return [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    ]


def solve(heights, start, end):
    d_h = len(heights)
    d_w = len(heights[0])

    def at(p):
        x, y = p
        if min(x, y) < 0 or y >= d_h or x >= d_w:
            return 999
        return heights[y][x]
    memory = {start: 0}

    target = at(start)
    positions = []
    for y, row in enumerate(heights):
        for x, h in enumerate(row):
            if h == target:
                heappush(positions, (0, target, (x, y)))
    
    while len(positions) > 0:
        steps, height, pos = heappop(positions)
        print(pos, chr(height), steps)
        steps += 1
        candidates = alternatives(pos)
        candidates = [c for c in candidates if c not in memory or memory[c] > steps]
        for c in candidates:
            h = at(c)
            if h > height + 1:
                continue
            memory[c] = steps
            heappush(positions, (steps, h, c))
    return memory[end]


def read(filename):
    start = None
    end = None
    heights = []
    with open(filename, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()]
        for row in rows:
            if 'S' in row:
                start = (row.rfind('S'), len(heights))
                row = row.replace('S', 'a')
            if 'E' in row:
                end = (row.rfind('E'), len(heights))
                row = row.replace('E', 'z')
            h = [ord(a) for a in row]
            heights.append(h)
    return heights, start, end


def main(filename):
    heights, start, end = read(filename)
    return solve(heights, start, end)


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("\n{}".format(main('input.txt')))
    else:
        for f in sys.argv[1:]:
            print("\n{}".format(main(f)))
