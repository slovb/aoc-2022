class Op:
    def __init__(self, left, right, op, reference_table):
        self.left = left
        self.right = right
        self.op = op
        self.reference_table = reference_table
        self.memory = None
    
    def evaluate(self):
        if self.memory is None:
            l = self.reference_table[self.left].evaluate()
            r = self.reference_table[self.right].evaluate()
            self.memory = self.op(l, r)
        return self.memory

class Val:
    def __init__(self, value):
        self.memory = value

    def evaluate(self):
        return self.memory


def solve(data):
    return data['root'].evaluate()


def read(path):
    data = {}
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
    }
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
                job = Op(left, right, ops[optext], data)
            data[name] = job
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
