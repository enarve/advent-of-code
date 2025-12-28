import math

class Point():
    def __init__(self, x, y, z, circuit):
        self.x = x
        self.y = y
        self.z = z
        self.circuit = circuit
    
    def description(self):
        return f'Point ({self.x}, {self.y}, {self.z}) in circuit {self.circuit}'

    def __str__(self):
        return self.description()
    
    def __repr__(self):
        return self.description()

def distance_between(first: Point, second: Point):
    return round(math.sqrt((first.x - second.x)**2
            + (first.y - second.y)**2
            + (first.z - second.z)**2))

def build_distances_matrix(points):
    matrix = []
    points_range = range(0, len(points))
    for i in points_range:
        row = []
        for j in points_range:
            if i < j:
                row.append(distance_between(points[i], points[j]))
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def find_closest_points(points, distances):
    zeroes_row = [0]*len(points)
    distances_without_zeroes = list(filter(lambda x: x!=zeroes_row, distances))
    # if distances_without_zeroes:
    #     for row in distances_without_zeroes:
    #         print(row)
    # print()
    min_dist: int = min(min(list(filter(lambda x: x > 0, row))) for row in distances_without_zeroes)
    x = (0, 0)
    for i, row in enumerate(distances):
        for j, value in enumerate(row):
            if value == min_dist:
                x = (i, j)
    (i, j) = x
    # print(points[i])
    # print(points[j])
    # print('Distance:', min_dist)
    return (i, j)

def connect_points(i: int, j: int, points: list[Point], distances: list[list[int]]):
    circuit_id = min(points[i].circuit, points[j].circuit)
    for index in [i, j]:
        if points[index].circuit != circuit_id:
            old_id =points[index].circuit
            # print(f'{points[i].circuit} -> {circuit_id}')
            for point in list(filter(lambda x: x.circuit == old_id , points)):
                point.circuit = circuit_id
            
    distances[i][j] = 0
    size = circuit_size(circuit_id, points)
    # print(f'{size} connections in circuit {circuit_id}!')

def count_circuits(points: list[Point]):
    c_dict = {}
    for point in points:
        c = point.circuit
        if c_dict.get(c):
            c_dict[c] += 1
        else:
            c_dict[c] = 1
    c_list = list(reversed(sorted(list(filter(lambda x: x[1] > 0, c_dict.items())), key=lambda x: x[1])))
    number_of_circuits = len(c_list)
    print(f'{number_of_circuits} circuits left')
    # res = c_list[0][1] * c_list[1][1] * c_list[2][1]
    return number_of_circuits

def circuit_size(id: int, points: list[Point]):
    counter = 0
    for point in points:
        if point.circuit == id:
            counter += 1
    return counter

# MARK: Main
def main():
    filename = 'input.txt'
    
    points: list[Point] = []
    distances: list[list[int]] = []

    with open(filename, 'r') as input:
        for (index, line) in enumerate(input.readlines()):
            coordinates = list(map(lambda x: int(x), line.split(',')))
            point = Point(x=coordinates[0], y=coordinates[1], z=coordinates[2], circuit=index)
            points.append(point)

        distances = build_distances_matrix(points)
        number_of_circuits = len(points)

        print('Started to connect circuits...')
        i, j = 0, 0
        while number_of_circuits != 1:
            i, j = find_closest_points(points, distances)
            connect_points(i, j, points, distances)
            # print()

            number_of_circuits = count_circuits(points)
        a = points[i].x
        b = points[j].x
        print(f'a: {a}, b: {b}, res: {a*b}')

if __name__ == '__main__':
    main()