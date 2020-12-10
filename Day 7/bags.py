def search_bags(inner_bags):
    global bags_sum, path
    for d in inner_bags.keys():
        if d == ' other':
            break
        if d == 'shiny gold':
            path.append(d)
            bags_sum += int(inner_bags[d])
            results.append([bags_sum, path])
            results_colors.append(path[0])
            continue
        else:
            path.append(d)
            bags_sum += int(inner_bags[d])
            for a in bags:
                if a[0] == d:
                    search_bags(a[1])
                    break
        path = path[:-1]
        bags_sum -= int(inner_bags[d])


def shiny_bag_rec(shiny_bags):
    global shiny_count, shiny_path, shiny_path_colors
    for d in shiny_bags:
        shiny_path_colors.append(d)
        shiny_path.append(shiny_bags[d])
        if d == ' other':
            global_shiny_path.append([shiny_path_colors, shiny_path])
        else:
            for a in bags:
                if a[0] == d:
                    shiny_bag_rec(a[1])
        shiny_path_colors = shiny_path_colors[:-1]
        shiny_path = shiny_path[:-1]


def sum_res(arr):
    sums_dict = {}
    for item in arr:
        g_sum = 1
        sums_path = []
        for w in range(0, len(item[1])):
            g_sum *= int(item[1][w])
            sums_path.append(item[0][w])
            t = tuple(sums_path)
            sums_dict[t] = g_sum
    return sums_dict

        
results = []
results_colors = []
bags_sum = shiny_count = 0
path = []
shiny_path = []
shiny_path_colors = []
global_shiny_path = []

with open('bags.txt', 'r') as f:
    bags = []
    for line in f:
        procLine = {}
        array = line.rstrip()[:-1].split(' bags contain ')
        temp = array[1].split(', ')
        for i in temp:
            procLine[i[2:i.index('bag') - 1]] = i[0]
        bags.append([array[0], procLine])


for b in bags:
    path.append(b[0])
    search_bags(b[1])
    path = []
    bags_sum = 0
results_colors = list(set(results_colors))
print(len(results_colors))

shiny = list(filter(lambda x: x[0] == 'shiny gold', bags))
shiny_bag_rec(shiny[0][1])
for g in global_shiny_path:
    g[0].pop()
    g[1].pop()
dict = sum_res(global_shiny_path)
print(sum(dict.values()))
