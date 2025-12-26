with open('input.txt', 'r') as input:
    counter = 0
    largest_id = 0
    input_parts = input.read().split('\n\n')
    fresh_ranges = list(map(lambda x: range(int(x.split('-')[0]), int(x.split('-')[1])+1), input_parts[0].split('\n')))
    fresh_ranges.sort(key=lambda x: x.start)
    for range in fresh_ranges:
        left_bound = range[0] if range[0] > largest_id else largest_id+1
        right_bound = range[-1]+1 if range[-1]+1 > largest_id else 0
        if left_bound < right_bound:
            counter += (right_bound-left_bound)
        if range[-1] > largest_id:
            largest_id = range[-1]
    print(f'Number of fresh ingredients: {counter}')