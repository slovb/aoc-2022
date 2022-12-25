def snafuToDecimal(snafu):
    n = 0
    for i, s in enumerate(snafu[::-1]):
        if s in ['2', '1', '0']:
            d = int(s)
        elif s == '-':
            d = -1
        else:
            d = -2
        n += d * (5**i)
    return n


def decimalToSnafu(dec):
    # print(dec)
    assert dec >= 0
    if dec == 0:
        return '0'
    parts = []
    while dec > 0:
        parts.append(dec % 5)
        dec //= 5
    # print(parts)
    for i in range(len(parts) - 1):  # do the last separately as it might need an append
        d = parts[i]
        if d > 2:
            parts[i] -= 5
            parts[i + 1] += 1
    # print(parts)
    if parts[-1] > 2:
        parts[-1] -= 5
        parts.append(1)
    # print(parts)
    output = []
    for d in parts[::-1]:  # reversing it to get the print order
        if d == -1:
            output.append('-')
        elif d == -2:
            output.append('=')
        else:
            output.append(str(d))
    return ''.join(output)


def solve(data):
    # print(data)
    return decimalToSnafu(sum(data))


def read(path):
    with open(path, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()] 
        return [snafuToDecimal(row) for row in rows]


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
