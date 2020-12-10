def summarize(arr, n):
    count = 0
    for a in arr:
        if a[1] == n:
            count += 1
    return count


with open("joltage.txt", "r") as f:
    adapters = sorted([int(line) for line in f.readlines()])
    adapters = [0] + adapters + [adapters[-1] + 3]

start = 0
result = []
for i in adapters:
    result.append([i, i - start])
    start = i
print(result)
print(summarize(result, 1) * summarize(result, 3))
paths = {adapters[0]: 1}
for x in adapters[1:]:
    paths[x] = sum(paths[x-y] for y in range(1, 4) if x-y in paths)
print(paths[adapters[-1]])
