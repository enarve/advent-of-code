import itertools

def parse_instruction(instruction: str):
    splitted = instruction.split()
    joltage = splitted.pop(-1)
    indicators = list(map(lambda x: x == '#', list(splitted.pop(0).replace('[', '').replace(']', ''))))
    buttons = list(map(lambda x: list(map(lambda y: int(y), x.replace('(', '').replace(')', '').split(','))), splitted))
    return indicators, buttons, joltage

def number_of_presses(instruction: str):
    res = None
    indicators, buttons, _ = parse_instruction(instruction)

    
    counter = 1

    while counter <= len(buttons):
        combinations = get_combinations(buttons, counter)
        for combination in combinations:
            number = 0
            lights = [False] * len(indicators)
            for button in list(combination):
                apply_button(button, lights)
                number += 1
            if lights == indicators:
                print(lights, indicators, number)
                print(f'Found combination! {list(combination)}')
                
                if not res:
                    res = number
                else:
                    if number < res:
                        res = number
        counter += 1

    return res

def get_combinations(buttons, number):
    return list(itertools.combinations(buttons, number))

def apply_button(button, lights):
    for index in button:
        lights[index] = not lights[index]

def main():
    total_number = 0
    with open('input.txt', 'r') as input:
        lines = input.readlines()
        for line in lines:
            total_number += number_of_presses(line)
            print(f'Number of presses: {total_number}.')
    print(f'Total number: {total_number}')

if __name__ == '__main__':
    main()