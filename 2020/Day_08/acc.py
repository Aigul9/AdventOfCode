def cycle(arr):
    global fl
    i = 0
    acc = 0
    sum_prev = 0
    while True:
        try:
            arr[i][2] = 1
            if arr[i][0] == 'nop':
                i += 1
            if arr[i][0] == 'acc':
                acc += int(arr[i][1])
                i += 1
            if arr[i][0] == 'jmp':
                i += int(arr[i][1])
            if sum(row[2] for row in arr) == sum_prev:
                for j in arr:
                    j[2] = 0
                return acc, arr
            sum_prev = sum(row[2] for row in arr)
        except IndexError:
            fl = True
            return acc, arr


def change(item):
    if item == 'nop':
        item = 'jmp'
    elif item == 'jmp':
        item = 'nop'
    return item


with open('acc.txt', 'r') as f:
    accs = [[l.split()[0], l.split()[1], 0] for l in f.readlines()]

print(cycle(accs)[0])
fl = False
for a in accs:
    if a[0] == 'acc':
        continue
    a[0] = change(a[0])
    res = cycle(accs)
    if fl:
        print(res[0])
        break
    else:
        a[0] = change(a[0])
