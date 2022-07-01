import re
from math import prod


def contains(ticket):
    local_result = {index: [] for index in range(len(fields))}
    for t_ind in range(len(ticket)):
        for key, fld in fields.items():
            if ticket[t_ind] in range(fld[0], fld[1] + 1) or ticket[t_ind] in (range(fld[2], fld[3] + 1)):
                local_result[t_ind].append(key)
    return local_result


with open('tickets.txt', 'r') as f:
    data = [line.splitlines() for line in f.read().split('\n\n')]
    fields, nearby_tickets, ranges = {}, [], set()
    for i in data[0]:
        name, values = i.split(': ')
        val = list(map(int, re.findall(r'(\d+)-(\d+) or (\d+)-(\d+)', values)[0]))
        fields[name] = val
        ranges = ranges.union(range(val[0], val[1] + 1)).union(range(val[2], val[3] + 1))
    my_ticket = list(map(int, data[1][1].split(',')))
    for i in range(1, len(data[2])):
        nearby_tickets.append(list(map(int, data[2][i].split(','))))

print(sum(n for t in nearby_tickets for n in t if n not in ranges))
result = contains(my_ticket)
for t in nearby_tickets:
    isValid = True
    for n in t:
        if n not in ranges:
            isValid = False
            break
    if isValid:
        local = contains(t)
        for j in result.keys():
            result[j] = list(set(result[j]).intersection(set(local[j])))

result = dict(sorted(result.items(), key=lambda k: len(k[1])))
prev = []
for k in result.keys():
    result[k] = [x for x in result[k] if x not in prev][0]
    prev.append(result[k])
print(prod([my_ticket[k] for k, v in result.items() if v.startswith('departure')]))
