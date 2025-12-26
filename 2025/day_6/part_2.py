with open('input.txt', 'r') as input:
    lines = list(map(lambda x: list(x.replace('\n', '') + ' '), input.readlines()))
    length = len(lines[0])
    height = len(lines)
    operations_index = height - 1
    total_sum = 0
    current_operation = '+'
    
    res = 0
    for i in range(0, length):
        numstring = ''
        for j in reversed(range(0, height)):
            
            if j == operations_index:
                operation = lines[operations_index][i]
                if operation in ['+', '*']:
                    # print(operation)
                    current_operation = operation
                    if current_operation == '+':
                        res = 0
                    elif current_operation == '*':
                        res = 1
            else:
                x = lines[j][i]
                if x != ' ':
                    numstring += x
                    
        if numstring.strip():
            num = int(numstring[::-1].strip())
            # print(num)
            if current_operation == '*':
                res *= num
            elif current_operation == '+':
                res += num
        else:
            # print('=', res)
            # print()
            total_sum += res
            res = 0

    print(f'Total sum is {total_sum}')
