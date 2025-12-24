def get_invalids(range):
    invalids = []
    for i in range:
        if check_if_invalid(i):
            invalids.append(i)
    print(f'{len(invalids)} invalids in {range[0]}-{range[len(range)-1]}: {invalids}')
    print()
    return invalids

def check_if_invalid(i):
    s = str(i)
    # print()
    # print('id:', s)
    invalid = False
    for j in range(1, len(s)//2 + 1):
        # print('bit length:', j)
        if len(s) % j == 0:
            n = len(s)//j
            # print('number of bits:', n)
            flag = True
            first = s[0:j]
            # print('first bit:', first)
            for k in range(2, n+1):
                k_bit = s[(k-1)*j:k*j]
                # print(f'bit {k}:', k_bit)
                if k_bit != first:
                    flag = False
                    break
            if flag:
                invalid = True
                # print('invalid!')
                break
    return invalid

with open('input.txt', 'r') as input:
    invalids = []
    ranges = map(lambda x: range(int(x.split('-')[0]), int(x.split('-')[1]) + 1),
        input.read().split(','))
    for r in ranges:
        invalids += get_invalids(r)
    s = 0
    for i in invalids:
        s += i
    print('Invalids:', len(invalids))
    print('Sum:', s)