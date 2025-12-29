def square_area(a, b):
    length = abs(a[0] - b[0]) + 1
    height = abs(a[1] - b[1]) + 1
    area = length * height
    return area

def main():
    with open('input.txt', 'r') as input:
        lines = input.readlines()
        points = list(map(lambda x: (int(x.strip().split(',')[0]), int(x.strip().split(',')[1])), lines))
        largest_area = 0
        for i, point_a in enumerate(points):
            for j, point_b in enumerate(points):
                if i < j:
                    area = square_area(point_a, point_b)
                    if area > largest_area:
                        print(point_a, point_b, 'area:', area)
                        largest_area = area

        print(f'Largest area: {largest_area}')

if __name__ == '__main__':
    main()