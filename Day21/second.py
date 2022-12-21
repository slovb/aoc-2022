ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
}


class Equation:
    def __init__(self, operation, target):
        self.left = operation.left
        self.right = operation.right
        self.op = operation.op
        self.memory = operation.memory
        self.tainted = operation.tainted
        self.target = target

    def evaluate(self):
        if self.memory is None:
            lval = self.left.evaluate()
            rval = self.right.evaluate()
            self.memory = self.op(lval, rval)
            if not self.tainted and self.left.tainted or self.right.tainted:
                self.tainted = True  # the cache invalidation spreads
        return self.memory == self.target

    def invalidate(self):
        if self.tainted:
            self.memory = None
            self.left.invalidate()
            self.right.invalidate()


class Operation:
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op
        self.memory = None
        self.tainted = False

    def evaluate(self):
        if self.memory is None:
            lval = self.left.evaluate()
            rval = self.right.evaluate()
            self.memory = self.op(lval, rval)
            if not self.tainted and self.left.tainted or self.right.tainted:
                self.tainted = True  # the cache invalidation spreads
        return self.memory

    def invalidate(self):
        if self.tainted:
            self.memory = None
            self.left.invalidate()
            self.right.invalidate()


class Val:
    def __init__(self, value):
        self.memory = value
        self.tainted = False

    def evaluate(self):
        return self.memory

    def invalidate(self):
        if self.tainted:
            self.memory = None


def solve(data):
    root = data['root']
    humn = data['humn']

    memory = {}

    def evaluate(i):
        if i not in memory:
            root.invalidate()
            humn.memory = i
            memory[i] = (root.evaluate(), root.memory)
        return memory[i]

    def find():
        i = 0
        step = 100

        is_solved, prev_diff = evaluate(i)
        if is_solved:
            return humn.memory
        print(f'BAD: {i}, {root.memory}')

        while True:
            is_solved, diff = evaluate(i + step)
            if is_solved:
                return humn.memory
            print(f'BAD: {i + step}, {root.memory}')
            if abs(diff) <= abs(prev_diff) and diff * prev_diff > 0:
                step *= 2
                prev_diff = diff
            else:
                print('Overstepped')
                i += step // 2
                step = 1
    i = find()
    print(f'GOOD: {i}')
    while evaluate(i - 1)[0]:
        i -= 1
        print(f'GOOD: {i}')
    return i


def read(path):
    data = {}

    with open(path, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()]
        for row in rows:
            name, rest = row.split(':')
            rest = rest[1:]
            parts = rest.split(' ')
            if len(parts) == 1:
                job = Val(int(rest))
            else:
                left, optext, right = parts
                job = Operation(left, right, ops[optext])
            data[name] = job
        for job in data.values():
            if isinstance(job, Operation):
                job.left = data[job.left]
                job.right = data[job.right]
        data['root'].op = ops['-']
        data['root'] = Equation(data['root'], 0)  # left - right = 0
        data['humn'].tainted = True
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
