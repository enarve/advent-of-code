with open('input.txt', 'r') as input:
    counter = 0
    input_parts = input.read().split('\n\n')
    fresh_ranges = list(map(lambda x: range(int(x.split('-')[0]), int(x.split('-')[1])+1), input_parts[0].split('\n')))
    available_ids = list(map(lambda x: int(x), input_parts[1].split('\n')))
    for id in available_ids:
        for range in fresh_ranges:
            if id in range:
                counter += 1
                break
    print(f'Number of fresh ingredients: {counter}')