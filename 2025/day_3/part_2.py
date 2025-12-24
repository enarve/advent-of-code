def find_largest_joltage(bank):
    sequence = ''
    previous_index = -1
    quantity = 12
    for i in range(1, quantity + 1):
        bank_segment = ''
        if i < quantity:
            bank_segment = bank[previous_index+1:-(quantity-i)]
        else:
            bank_segment = bank[previous_index+1:]
        m = max(bank_segment)
        sequence += m
        previous_index += 1
        previous_index += bank_segment.index(m)
    return int(sequence)

with open('input.txt', 'r') as input:
    total_joltage = 0
    for bank in input.readlines():
        total_joltage += find_largest_joltage(bank.strip())
    print(f'Total output joltage: {total_joltage}')