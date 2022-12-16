import copy


start_time = 26
start_valve = 'AA'


def complete(valves):
    num_valves = len(valves)
    is_complete = False
    while not is_complete:
        is_complete = True
        for key, valve in valves.items():
            new_edges = {}
            for neighbor, cost in valve['edges'].items():
                if neighbor in new_edges:
                    new_edges[neighbor] = min(cost, new_edges[neighbor])
                else:
                    new_edges[neighbor] = cost
                for edge, added_cost in valves[neighbor]['edges'].items():
                    if edge == key:
                        continue
                    if edge in new_edges:
                        new_edges[edge] = min(cost + added_cost, new_edges[edge])
                    else:
                        new_edges[edge] = cost + added_cost
            valve['edges'] = new_edges
            if len(new_edges) < num_valves - 1:
                is_complete = False


def sorted_edges(valves, edges):
    def key(edge):
        name, cost = edge
        return valves[name]['rate'] * (start_time - cost)
    return dict(sorted(edges.items(), key=key, reverse=True))


def clean(valves, starter_costs):
    baddies = [name for name, valve in valves.items() if valve['rate'] == 0]
    for baddie in baddies:
        del valves[baddie]
        del starter_costs[baddie]
    for valve in valves.values():
        for baddie in baddies:
            del valve['edges'][baddie]
        valve['edges'] = sorted_edges(valves, valve['edges'])


def find_starter_costs(valves):
    costs = copy.deepcopy(valves[start_valve]['edges'])
    costs[start_valve] = 0
    costs = sorted_edges(valves, costs)
    return costs


def score(valves, starter_costs, candidate):
    costs = starter_costs
    time = start_time
    score = 0
    for name in candidate:
        time -= costs[name] + 1
        if time <= 0:
            break
        score += time * valves[name]['rate']
        costs = valves[name]['edges']
    return score


def search(valves, time, costs, current=[], taken=None):
    # count = 0
    for name, cost in costs.items():
        if taken is not None and name in taken:
            continue
        if name in current:
            continue
        if time - cost - 1 > 0:
            candidates = search(valves, time - cost - 1, valves[name]['edges'], current + [name], taken)
            if candidates is not None:
                for candidate in candidates:
                    # count += 1
                    yield candidate
    # if count == 0:
        # yield current  # too greedy for test, but works on live
    yield current


def solve(valves):
    complete(valves)
    starter_costs = find_starter_costs(valves)
    clean(valves, starter_costs)
    best_score = 0
    i, j = 0, 0

    def scr(candidate):
        return score(valves, starter_costs, candidate)
    for candidate in search(valves, start_time, starter_costs):
        i += 1
        candidate_score = scr(candidate)
        if candidate_score < best_score // 2:
            continue
        banned = set(candidate)
        for elephant in search(valves, start_time, starter_costs, [], banned):
            j += 1
            value = candidate_score + scr(elephant)
            if value > best_score:
                best_score = value
                print(f'{i} {j}: {best_score}')
                if candidate_score < best_score // 2:
                    break
    print(f'iterations: {i} {j}')
    return best_score


def read(path):
    with open(path, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()]
        nodes = {}
        for row in rows:
            parts = row.split(' ')
            name = parts[1]
            rate = int(parts[4][5:-1])
            edges = {edge.rstrip(','): 1 for edge in parts[9:]} 
            nodes[name] = {
                'name': name,
                'rate': rate,
                'edges': edges,
            }
    return nodes


def main(path, is_test):
    data = read(path)
    return solve(data)


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
