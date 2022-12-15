def merge(segments):
    output = []
    segments = sorted(segments)
    # print(' ')
    # print(segments)
    # print(' ')
    left = segments[0]
    for right in segments[1:]:
        if left[1] + 1 < right[0]:
            # print(f"can't merge {left} and {right}")
            output.append(left)
            left = right
        else:
            # print(f'merge {left} with {right} into {(left[0], right[1])}')
            left = (left[0], max(left[1], right[1]))
    output.append(left)
    return output


def solve(data, target):
    to_remove = set()
    segments = []

    for sensor, beacon in data:
        s_x, s_y = sensor
        b_x, b_y = beacon
        if b_y == target:
            to_remove.add(beacon)
        r = abs(b_x - s_x) + abs(b_y - s_y)
        if s_y + r < target or s_y - r > target:
            continue
        d = r - abs(target - s_y)
        segments.append((s_x - d, s_x + d))
        print(f'S: {sensor}, B: {beacon} becomes {segments[-1]}')
    segments = merge(segments)
    size = 0
    for seg in segments:
        size += 1 + seg[1] - seg[0]
    return size - len(to_remove)


def read_pos(text):
    _, rest0, y = text.split('=')
    x, _ = rest0.split(',')
    return (int(x), int(y))


def read(path):
    sensors = []
    with open(path, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()]
        for row in rows:
            sensor, beacon = row.split(':')
            sensors.append((read_pos(sensor), read_pos(beacon)))
    return sensors


def main(path, is_test):
    data = read(path)
    target = 10 if is_test else 2000000
    return solve(data, target)


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
