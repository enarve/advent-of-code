with open('input.txt', 'r') as input:
    lines = list(map(lambda x: x.strip(), input.readlines()))
    firstline = lines[0]
    start_index = firstline.index('S')
    beams = [start_index]
    split_counter = 0
    for line in lines:
        for (i, s) in enumerate(line):
            if s == '^' and i in beams:
                split_counter += 1
                beams.remove(i)
                if i-1 >= 0:
                    if i-1 not in beams:
                        beams.append(i-1)
                if i+1 <= len(line)-1:
                    if i+1 not in beams:
                        beams.append(i+1)

    print(f'Total number of splits: {split_counter}')
