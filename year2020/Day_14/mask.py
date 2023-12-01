import re


with open('mask.txt', 'r') as f:
    memory = {}
    lines = [line.rstrip() for line in f]
    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
        else:
            ind, val = list(map(int, re.findall(r'(\d+)', line)))
            val = str(bin(val)[2:].zfill(36))
            result = ''
            for i in range(len(mask)):
                result += mask[i] if mask[i] != 'X' else val[i]
            memory[ind] = result

for k, v in memory.items():
    memory[k] = int(v, 2)
print(sum(memory.values()))
