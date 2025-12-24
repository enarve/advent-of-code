def find_largest_joltage(bank):
    first = max(bank[:-1])
    first_index = bank[:-1].index(first)
    second = max(bank[first_index+1:])
    pair = first + second
    return int(pair)

with open('input.txt', 'r') as input:
    total_joltage = 0
    for bank in input.readlines():
        total_joltage += find_largest_joltage(bank.strip())
    print(f'Total output joltage: {total_joltage}')