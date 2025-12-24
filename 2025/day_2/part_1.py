def get_invalids(range):
    invalids = []
    for i in range:
        if check_if_invalid(i):
            invalids.append(i)
    return invalids

def check_if_invalid(i):
    s = str(i)
    if len(s) % 2 == 0:
        mid = (len(s)//2)
        end = len(s) + 1
        if s[0:mid] == s[mid:end]:
            return True
    return False

with open('input.txt', 'r') as input:
    invalids = []
    ranges = map(lambda x: range(int(x.split('-')[0]), int(x.split('-')[1]) + 1),
        input.read().split(','))
    for r in ranges:
        invalids += get_invalids(r)
    s = 0
    for i in invalids:
        s += i
    print(s)
    