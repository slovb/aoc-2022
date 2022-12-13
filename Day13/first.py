import json


def compare(a, b):
    print(f'Compare {a} vs {b}')
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            print('Left is smaller')
            return 1
        elif a == b:
            return 0
        else:
            print('Right is smaller')
            return -1
    if isinstance(a, int) and isinstance(b, list):
        print('Mixed types convert left')
        return compare([a], b)
    if isinstance(a, list) and isinstance(b, int):
        print('Mixed types convert right')
        return compare(a, [b])
    i = 0
    la = len(a)
    lb = len(b)
    while True:
        if i == la == lb:
            return 0
        elif i == la:
            print('Left ran out')
            return 1
        elif i == lb:
            print('Right ran out')
            return -1
        cmp = compare(a[i], b[i])
        if cmp != 0:
            return cmp
        i += 1


def solve(input):
    i = 1
    output = 0
    for a, b in input:
        cmp = compare(a, b)
        if cmp == 1:
            output += i
        print(cmp)
        print(' ')
        i += 1
    return output


def read(filename):
    input = []
    with open(filename, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()]
        while len(rows) > 0:
            a = json.loads(rows.pop(0))
            b = json.loads(rows.pop(0))
            if len(rows) > 0:
                rows.pop(0)
            input.append((a, b))
    return input


def main(filename):
    input = read(filename)
    return solve(input)


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("\n{}".format(main('input.txt')))
    else:
        for f in sys.argv[1:]:
            print("\n{}".format(main(f)))
