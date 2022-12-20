class Item:
    def __init__(self, value):
        self.next = None
        self.back = None
        self.value = value

    def move_forward(self):
        item = self.next
        far_back = self.back
        far_front = item.next

        far_back.next = item

        item.back = far_back
        item.next = self
        self.back = item
        self.next = far_front

        far_front.back = self

    def move_backward(self):
        item = self.back
        far_back = item.back
        far_front = self.next

        far_back.next = self

        self.back = far_back
        self.next = item
        item.back = self
        item.next = far_front

        far_front.back = item


def solve(start, items):
    zero = None
    # num_items = len(items)
    for item in items:
        if item.value == 0:
            zero = item
            continue
        repeats = abs(item.value)
        # repeats = item.value % num_items
        # if item.value < 0:
        #     repeats -= num_items
        for _ in range(repeats):
            if item.value > 0:
                if item == start:
                    start = item.next
                elif item.next == start:
                    start = item
                item.move_forward()
            else:
                if item == start:
                    start = item.next  # unsure
                elif item.back == start:
                    start = item
                item.move_backward()
    values = []
    item = zero
    for _ in range(3):
        for _ in range(1000):
            item = item.next
        values.append(item.value)
    return sum(values)


def read(path):
    with open(path, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()]
        values = [int(row) for row in rows]
        start = Item(values[0])
        items = [start]
        prev = start
        for value in values[1:]:
            item = Item(value)
            items.append(item)
            item.back = prev
            prev.next = item
            prev = item
        prev.next = start
        start.back = prev
        return start, items


def main(path, is_test):
    start, items = read(path)
    return solve(start, items)


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
