def is_visible(idx, value, array):
    return max(array[:idx]) < value or value > max(array[idx+1:])


def get_scenic_score(idx, value, array):
    first, second = list(reversed(array[:idx])), array[idx+1:]

    count_f = len(first)
    for t in range(len(first)):
        if first[t] >= value:
            count_f = t + 1
            break

    count_s = len(second)
    for t in range(len(second)):
        if second[t] >= value:
            count_s = t + 1
            break

    return count_f * count_s


with open('input.txt', 'r') as f:
    trees = []
    for line in f.readlines():
        trees.append(list(map(int, list(line.strip()))))

num_visible = (len(trees) + len(trees[1:-1])) * 2
max_score = 0
for i in range(1, len(trees) - 1):
    for j in range(1, len(trees[0]) - 1):
        val = trees[i][j]
        if is_visible(j, val, trees[i]) or is_visible(i, val, [k[j] for k in trees]):
            num_visible += 1
        row_score = get_scenic_score(j, val, trees[i])
        col_score = get_scenic_score(i, val, [k[j] for k in trees])
        max_score = max(max_score, row_score * col_score)

print(num_visible)
print(max_score)
