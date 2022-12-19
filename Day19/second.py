duration = 32


class Memory():
    def __init__(self, actions):
        self.value = 0
        self.actions = actions
        self.max_production = [max([cost[i] for _, cost in actions]) for i in range(3)]

    def store(self, value):
        if value > self.value:
            # print(value)
            self.value = value

    def is_bad_branch(self, time, production, inventory):
        # check if production is running rampant
        for i in range(3):
            if production[i] > self.max_production[i]:
                return True
        # check if maximum value won't exceed current best
        v = inventory[-1] + production[-1]*time
        v += time * (time + 1) // 2
        if v <= self.value:
            return True
        return False


def can_afford(cost, inventory):
    return all([cost[i] <= inventory[i] for i in range(4)])


def search(actions, time, production, inventory, memory):
    if time == 0:
        memory.store(inventory[-1])
        return inventory[-1]
    if memory.is_bad_branch(time, production, inventory):
        return -1
    results = []
    unaffordable_actions = []
    for action in actions:  # handle the wait action separately
        production_increase, cost = action
        if can_afford(cost, inventory):
            new_production = tuple([production[i] + production_increase[i] for i in range(4)])
            new_inventory = tuple([production[i] + inventory[i] - cost[i] for i in range(4)])
            results.append(search(memory.actions, time - 1, new_production, new_inventory, memory))
        else:
            unaffordable_actions.append(action)

    if len(unaffordable_actions) > 0:
        new_inventory = tuple([production[i] + inventory[i] for i in range(4)])
        results.append(search(unaffordable_actions, time - 1, production, new_inventory, memory))
    return max(results)


def score(blueprint):
    actions = [action for action in blueprint['robots'][::-1]]  # reverse order means more geodes
    production = (1, 0, 0, 0)
    inventory = (0, 0, 0, 0)
    memory = Memory(actions)
    return search(actions, duration, production, inventory, memory)


def solve(data):
    value = 1
    for blueprint in data:
        value *= score(blueprint)
    return value


def read(path):
    data = []
    with open(path, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()]
        for row in rows[:3]:
            start, rest = row.split(':')
            id = int(start.split(' ')[1])
            ore_robot, clay_robot, obsidian_robot, geode_robot, _ = rest.split('.')
            robots = (
                (
                    (1, 0, 0, 0),
                    (int(ore_robot.split(' ')[-2]), 0, 0, 0)
                ),
                (
                    (0, 1, 0, 0),
                    (int(clay_robot.split(' ')[-2]), 0, 0, 0)
                ),
                (
                    (0, 0, 1, 0),
                    (int(obsidian_robot.split(' ')[-5]), int(obsidian_robot.split(' ')[-2]), 0, 0)
                ),
                (
                    (0, 0, 0, 1),
                    (int(geode_robot.split(' ')[-5]), 0, int(geode_robot.split(' ')[-2]), 0)
                ),
            )
            data.append({
                'id': id,
                'robots': robots,
            })
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
