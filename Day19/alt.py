# duration = 24


# class Memory():
#     def __init__(self, actions):
#         self.value = 0
#         self.actions = actions
#         self.max_production = [max([cost[i] for _, cost in actions]) for i in range(3)]

#     def store(self, value):
#         if value > self.value:
#             print(value)
#             self.value = value

#     def avoid_overproduction(self, actions, production):  # remove overproduction
#         output = []
#         for action in actions:
#             production_increase, _ = action
#             new_production = tuple([production[i] + production_increase[i] for i in range(4)])
#             if not any([new_production[i] > self.max_production[i] for i in range(3)]):
#                 output.append(action)
#         return output


# def can_afford(cost, inventory):
#     return all([cost[i] <= inventory[i] for i in range(4)])


# def plus(a, b):
#     return tuple([a[i] + b[i] for i in range(4)])


# def minus(a, b):
#     return tuple([a[i] - b[i] for i in range(4)])


# def run(action, time, production, inventory, memory: Memory):
#     production_increase, cost = action
#     wait = 1
#     new_inventory = plus(production, inventory)
#     while not can_afford(cost, new_inventory):
#         new_inventory = plus(production, new_inventory)
#         wait += 1
#         if wait == time:
#             memory.store(new_inventory[-1])
#             return new_inventory[-1]
#     new_production = plus(production, production_increase)
#     new_inventory = minus(new_inventory, cost)
#     return plan(memory.actions, time - wait, new_production, new_inventory, memory)


# def plan(actions, time, production, inventory, memory: Memory):
#     if time == 0:
#         memory.store(inventory[-1])
#         return inventory[-1]
#     results = []
#     actions = memory.avoid_overproduction(actions, production)
#     for action in actions:
#         results.append(run(action, time, production, inventory, memory))
#     return max(results)


# def score(blueprint):
#     actions = [action for action in blueprint['robots'][::-1]]  # reverse order means more geodes
#     production = (1, 0, 0, 0)
#     inventory = (0, 0, 0, 0)
#     memory = Memory(actions)
#     return plan(actions, duration, production, inventory, memory)


# def solve(data):
#     quality = 0
#     for blueprint in data:
#         quality += blueprint['id'] * score(blueprint)
#     return quality


# def read(path):
#     data = []
#     with open(path, 'r') as f:
#         rows = [row.rstrip() for row in f.readlines()]
#         for row in rows:
#             start, rest = row.split(':')
#             id = int(start.split(' ')[1])
#             ore_robot, clay_robot, obsidian_robot, geode_robot, _ = rest.split('.')
#             robots = (
#                 (
#                     (1, 0, 0, 0),
#                     (int(ore_robot.split(' ')[-2]), 0, 0, 0)
#                 ),
#                 (
#                     (0, 1, 0, 0),
#                     (int(clay_robot.split(' ')[-2]), 0, 0, 0)
#                 ),
#                 (
#                     (0, 0, 1, 0),
#                     (int(obsidian_robot.split(' ')[-5]), int(obsidian_robot.split(' ')[-2]), 0, 0)
#                 ),
#                 (
#                     (0, 0, 0, 1),
#                     (int(geode_robot.split(' ')[-5]), 0, int(geode_robot.split(' ')[-2]), 0)
#                 ),
#             )
#             data.append({
#                 'id': id,
#                 'robots': robots,
#             })
#     return data


# def main(path, is_test):
#     data = read(path)
#     return solve(data)


# def display(output):
#     print('\n')
#     print(output)


# if __name__ == "__main__":
#     is_test = True
#     import os
#     dirname = os.path.realpath(os.path.dirname(__file__))
#     filename = 'test.txt' if is_test else 'input.txt'
#     path = f'{dirname}/{filename}'
#     import sys

#     if (len(sys.argv) < 2):
#         display(main(path, is_test=is_test))
#     else:
#         for f in sys.argv[1:]:
#             display(main(f))
