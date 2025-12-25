with open('input.txt', 'r') as input:
    rolls = list(map(lambda x: list(x.strip()), input.readlines()))
    width = len(rolls[0])
    height = len(rolls)
    # print(f'height: {height}, width: {width}')
    available_rolls = width * height
    removed_rolls = 0

    # find all available rolls
    while available_rolls != 0:
        available_rolls = 0
        for i in range(0, height):
            # print(rolls[i])
            for j in range(0, width):
                if rolls[i][j] == '@':
                    # count adjacent rolls
                    adjacent_rolls = 0
                    vertical_range = range((i-1 if i>0 else i), (i+2 if i<height-1 else i+1)) # [i-1, i, i+1]
                    horizontal_range = range((j-1 if j>0 else j), (j+2 if j<width-1 else j+1)) # [j-1, j, j+1]
                    for k in vertical_range:
                        for l in horizontal_range:
                            
                            if rolls[k][l] in ['@', 'x'] and not (k==i and l==j):
                                adjacent_rolls += 1
                    if adjacent_rolls < 4:
                        available_rolls += 1
                        rolls[i][j] = 'x'
        print(f'{available_rolls} rolls are available')

        # remove available rolls
        for i in range(0, height):
            for j in range(0, width):
                if rolls[i][j] == 'x':
                    rolls[i][j] = '.'
        removed_rolls += available_rolls

        # for line in rolls:
        #     print(line)

    print(f'{removed_rolls} rolls were removed')
    
    
