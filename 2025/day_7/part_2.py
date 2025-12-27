with open('input.txt', 'r') as input:
    lines = list(map(lambda x: x.strip(), input.readlines()))
    firstline = lines[0]
    start_index = firstline.index('S')
    current_beams = {start_index:1}
    timeline_counter = 1
    for line in lines:
        new_beams: dict[int:int] = {}
        for (i, s) in enumerate(line):
            if i in sorted(current_beams.keys()):
                if s == '^':
                    l = current_beams[i]
                    if i-1 >= 0 and i+1 <= len(line)-1:
                        timeline_counter += (1 * l)
                        # print(f'Beam {i}: {l} splits. Timelines: {timeline_counter}')
                    if i-1 >= 0:
                            if new_beams.get(i-1):
                                new_beams[i-1] += l
                            else:
                                 new_beams[i-1] = l
                    if i+1 <= len(line)-1:
                            if new_beams.get(i+1):
                                new_beams[i+1] += l
                            else:
                                 new_beams[i+1] = l
                    current_beams.pop(i)

        for (k, v) in new_beams.items():
            if current_beams.get(k):
                current_beams[k] += v
            else:
                current_beams[k] = v

        # if '^' in line or 'S' in line:
        #     print('Timelines:', timeline_counter)
        #     print('New beams:', sorted(list(current_beams.items())))
        #     print()
                
    print(f'Total number of splits: {timeline_counter}')
