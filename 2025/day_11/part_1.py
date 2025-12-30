class Device():
    def __init__(self, name: str, outputs: list[str]):
        self.name = name
        self.outputs = outputs

    def __str__(self):
        return f'{self.name}: {self.outputs}'
    
    def __repr__(self):
        return f'{self.name}: {self.outputs}'

def parse_devices(rows: list[str]):
    devices = []
    for row in rows:
        splitted = row.split(':')
        name = splitted[0]
        outputs = splitted[1].strip().split()
        device = Device(name, outputs)
        devices.append(device)
    return devices

def look_for_out(outputs: list[str]):
    global count
    global devices
    if 'out' in outputs:
        count += 1
    else:
        for output in outputs:
            device = list(filter(lambda x: x.name == output, devices))[0]
            look_for_out(device.outputs)

def main():
    global count
    global devices
    count = 0
    devices = []
    with open('test.txt', 'r') as input:
        lines = input.readlines()
        devices = parse_devices(lines)
    first_device = list(filter(lambda x: x.name == 'you', devices))[0]
    look_for_out(first_device.outputs)
    print(f'Ways out: {count}')

if __name__ == '__main__':
    main()