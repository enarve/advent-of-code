# Draft for 9.2

def square_area(a, b):
    length = abs(a[0] - b[0]) + 1
    height = abs(a[1] - b[1]) + 1
    area = length * height
    return area

def make_border_array(points):
    print('Making border...')
    border = []
    last_point = None
    for point in points + [points[0]]:
        if last_point:
            for i in [0, 1]:
                k = 0 if i == 1 else 1
                if last_point[i] == point[i]:
                    step = 1 if last_point[k] < point[k] else -1
                    for coord in range(last_point[k], point[k], step):
                        if i == 0:
                            x = (point[i], coord)
                            border.append(x)
                        else:
                            x = (coord, point[i])
                            border.append(x)
        last_point = point
    return border

def make_full_array(border):
    print('Making full array...')
    full_array = border
    min_x = min(map(lambda x: x[0], border))
    max_x = max(map(lambda x: x[0], border))
    min_y = min(map(lambda x: x[1], border))
    max_y = max(map(lambda x: x[1], border))

    for y in range(min_y, max_y + 1):
        flag = False
        lock = False
        for x in range(min_x, max_x + 1):
            print(f'Point {x}, {y}')
            if (x, y) in border:
                if not lock:
                    flag = not flag
                    lock = True
            else:
                lock = False
                if flag:
                    full_array.append((x, y))
        
    return full_array

def check_if_square_fits(point_a, point_b, good_points):
    res = True
    x_a = point_a[0]
    x_b = point_b[0]
    step = 1 if x_a < x_b else -1
    horizontal_range = range(x_a, x_b + step, step)

    y_a = point_a[1]
    y_b = point_b[1]
    step = 1 if y_a < y_b else -1
    vertical_range = range(y_a, y_b + step, step)
    print(point_a, point_b, vertical_range, horizontal_range)
    for i in [horizontal_range[0], horizontal_range[-1]]:
        for j in vertical_range:
            if (i, j) not in good_points:
                res = False
                break
    if res:
        for i in [vertical_range[0], vertical_range[-1]]:
            for j in horizontal_range:
                if (j, i) not in good_points:
                    res = False
                    break
    return res

def find_square(points, good_points):
    largest_area = 0
    counter = 0
    for i, point_a in enumerate(points):
        for j, point_b in enumerate(points):
            if i < j:
                area = square_area(point_a, point_b)
                if area > largest_area:
                    print(f'{counter}: Found something large: {area}')
                    counter += 1
                    if check_if_square_fits(point_a, point_b, good_points):
                        print(point_a, point_b, 'area:', area)
                        largest_area = area
                    else:
                        print(f'Does not fit! Still {largest_area}')
                        print()
    return largest_area

def main():
    with open('test.txt', 'r') as input:
        lines = input.readlines()
        points = list(map(lambda x: (int(x.strip().split(',')[0]), int(x.strip().split(',')[1])), lines))

        # make border array
        border = make_border_array(points)
        full_array = make_full_array(border)
        print(f'f_a {full_array}')

        largest_area = find_square(points, full_array)
        print()
        print(f'Largest area: {largest_area}')

if __name__ == '__main__':
    main()