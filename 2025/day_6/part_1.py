with open('input.txt', 'r') as input:
    lines = list(map(lambda x: x.split(), input.readlines()))
    length = len(lines[0])
    operations_index = len(lines)-1
    total_sum = 0

    for i in range(0, length):
        operation = lines[operations_index][i]
        res = 0
        if operation == '*':
            res = 1
            for j in range(0, operations_index):
                res *= int(lines[j][i])
        elif operation == '+':
            res = 0
            for j in range(0, operations_index):
                res += int(lines[j][i])
        total_sum += res

    print(f'Total sum is {total_sum}')
