from typing import List


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

    def forward(self, steps):
        item = self
        for _ in range(steps):
            item = item.next
        return item
    
    def backward(self, steps):
        item = self
        for _ in range(steps):
            item = item.back
        return item

    def pluck(self):
        self.back.next = self.next
        self.next.back = self.back

    def inject(self, item):
        self.back = item
        self.next = item.next
        item.next.back = self

        item.next = self


def debug(start):
    values = [start.value]
    item = start.next
    while item != start:
        values.append(item.value)
        item = item.next
    return values


def solve(items: List[Item]):
    zero = None
    num_items = len(items)
    for item in items:
        if item.value == 0:
            zero = item

        steps = abs(item.value) % (num_items - 1)
        if steps == 0:
            continue

        item.pluck()
        if item.value > 0:
            target = item.forward(steps)
        else:
            target = item.backward(steps + 1)
        item.inject(target)
    values = []
    item = zero
    for _ in range(3):
        item = item.forward(1000)
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
        return items


def main(path, is_test):
    items = read(path)
    return solve(items)


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
