def directions(p):
    x, y, z = p
    return [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ]


def solve(data):
    cloud = set()
    count = 0
    minX, minY, minZ = maxX, maxY, maxZ = data[0]
    for point in data:
        x, y, z = point
        minX = min(minX, x)
        minY = min(minY, y)
        minZ = min(minZ, z)
        maxX = max(maxX, x)
        maxY = max(maxY, y)
        maxZ = max(maxZ, z)
        count += 6
        for adjacent in directions(point):
            if adjacent in cloud:
                count -= 2
        cloud.add(point)

    def oob(point):
        x, y, z = point
        if x < minX or x > maxX:
            return True
        if y < minY or y > maxY:
            return True
        if z < minZ or z > maxZ:
            return True
        return False

    def search(point, visited):
        points = [point]
        while len(points) > 0:
            point = points.pop()
            if point in cloud or point in visited:
                continue
            if oob(point):
                return False
            visited.add(point)
            for adjacent in directions(point):
                points.append(adjacent)
        return True
    
    internal_points = set()
    for x in range(minX, maxX):
        for y in range(minY, maxY):
            for z in range(minZ, maxZ):
                point = (x, y, z)
                if point in internal_points or point in cloud:
                    continue
                visited = set()
                if search(point, visited):
                    for found in visited:
                        count -= 6
                        for adjacent in directions(found):
                            if adjacent in internal_points:
                                count += 2
                        internal_points.add(found)
    return count


def read(path):
    data = []
    with open(path, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()]
        for row in rows:
            data.append(tuple([int(c) for c in row.split(',')]))
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
