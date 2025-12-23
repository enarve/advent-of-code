# Find password from input.txt

state = 50
counter = 0

def update_state(code):
    global state
    letter = code[0]
    step = int(code[1:])
    direction = 1
    if letter == 'L':
        direction = -1
    s = state + (direction * step)
    while s < 0:
        s += 100
    if s > 99:
        s %= 100
    state = s

def update_counter():
    global state
    global counter
    if state == 0:
        counter += 1

def main():
    with open('input.txt', 'r') as input:
        for code in input:
            update_state(code)
            update_counter()
    print(f'Password: {counter}')

if __name__ == '__main__':
    main()