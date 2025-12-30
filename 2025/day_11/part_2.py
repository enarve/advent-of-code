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

def look_for_out(device, destination):
    global cache
    global devices
    name = device.name
    outputs = list(filter(lambda x: x != name, device.outputs))
    if destination != 'out' and name == 'out':
        return 0
    if destination in outputs:
        return 1
    else:
        res = 0
        if cache.get(name) != None:
            res = cache[name]
        else:
            for output in outputs:
                # check if exists in cache
                if cache.get(output) != None:
                    res += cache[output]
                else:
                    if output != 'out':
                        device = list(filter(lambda x: x.name == output, devices))[0]
                        res += look_for_out(device, destination)
            # went through all outputs
            # cache here
            cache[name] = res
        return res

def main():
    global devices
    global cache
    count = 0
    devices = []
    cache = {}
    with open('input.txt', 'r') as input:
        lines = input.readlines()
        devices = parse_devices(lines)
    you_device = list(filter(lambda x: x.name == 'you', devices))[0]

    svr_device = list(filter(lambda x: x.name == 'svr', devices))[0]
    fft_device = list(filter(lambda x: x.name == 'fft', devices))[0]
    dac_device = list(filter(lambda x: x.name == 'dac', devices))[0]
    
    print('you to out')
    you_to_out = look_for_out(you_device, 'out')
    print(you_to_out)
    cache = {}
    print()

    print('svr to fft')
    svr_to_fft = look_for_out(svr_device, 'fft')
    print(svr_to_fft)
    cache = {}
    print('fft to dac')
    fft_to_dac = look_for_out(fft_device, 'dac')
    print(fft_to_dac)
    cache = {}
    print('dac to out')
    dac_to_out = look_for_out(dac_device, 'out')
    print(dac_to_out)
    cache = {}
    a1 = svr_to_fft * fft_to_dac * dac_to_out
    print(a1)
    print()

    print('svr to dac')
    svr_to_dac = look_for_out(svr_device, 'dac')
    print(svr_to_dac)
    cache = {}
    print('dac to fft')
    dac_to_fft = look_for_out(dac_device, 'fft')
    print(dac_to_fft)
    cache = {}
    print('fft to out')
    fft_to_out = look_for_out(fft_device, 'out')
    print(fft_to_out)
    a2 = svr_to_dac * dac_to_fft * fft_to_out
    print(a2)
    print()

    count = a1 + a2

    print(f'Ways out: {count}')

if __name__ == '__main__':
    main()