def solve(monkeys):
    count = [0] * len(monkeys)
    for _ in range(20):
        for i in monkeys:
            monkey = monkeys[i]
            while len(monkey['items']) > 0:
                count[i] += 1
                item = monkey['items'].pop(0)
                item = monkey['operation'](item)
                item = item // 3
                test = item % monkey['test'] == 0
                to = monkey[test]
                monkeys[to]['items'].append(item)
    count.sort()
    return count[-1] * count[-2]


def read_val(a):
    if a == 'old':
        return lambda x: x
    x = int(a)
    return lambda _: x


def read_op(row):
    a, op, b = row.split(' ')[:3]
    x = read_val(a)
    y = read_val(b)
    if op == '+':
        return lambda z: x(z) + y(z)
    return lambda z: x(z) * y(z)


def read(filename):
    with open(filename, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()]
        monkeys = {}
        temp = {}
        for row in rows:
            if row == '':
                monkeys[temp['id']] = temp
                temp = {}
            elif row.startswith('Monkey '):
                temp['id'] = int(row.split(' ')[1].split(':')[0])
            elif row.startswith('  Starting items: '):
                parts = ''.join(row.split(' ')[4:]).split(',')
                temp['items'] = list(map(int, parts))
            elif row.startswith('  Operation:'):
                parts = row.split('=')[1].strip()
                temp['operation'] = read_op(parts)
            elif row.startswith('  Test:'):
                parts = row.split(' ')[-1]
                v = int(parts)
                # test = lambda x: (x % v) == 0
                temp['test'] = v
                # print(f'{2080} % {v} = {test(2080)}')
            elif row.startswith('    If true:'):
                parts = row.split(' ')[-1]
                temp[True] = int(parts)
            elif row.startswith('    If false:'):
                parts = row.split(' ')[-1]
                temp[False] = int(parts)
            else:
                raise Exception(row)
        monkeys[temp['id']] = temp
        temp = {}
        return monkeys


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
