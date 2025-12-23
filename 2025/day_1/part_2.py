state = 50
counter = 0

def update_state(code):
    global state
    global counter
    letter = code[0]
    steps = int(code[1:])
    direction = 1
    if letter == 'L':
        direction = -1
    dif = state + (direction * steps)
    s = dif % 100
    c = (abs(dif) // 100)
    if dif <= 0 and (state != 0 or s == 0):
        c += 1
    counter += c
    state = s
    print(code, state, counter)
    print()
    

def main():
    with open('input.txt', 'r') as input:
        for code in input:
            update_state(code.strip())
    print(f'Password: {counter}')

if __name__ == '__main__':
    main()