def directions(p):
    x, y, z = p
    return [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ]


def solve(data):
    cloud = set()
    count = 0
    for point in data:
        count += 6
        for adjacent in directions(point):
            if adjacent in cloud:
                count -= 2
        cloud.add(point)
    return count


def read(path):
    data = []
    with open(path, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()]
        for row in rows:
            data.append(tuple([int(c) for c in row.split(',')]))
    return data


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
