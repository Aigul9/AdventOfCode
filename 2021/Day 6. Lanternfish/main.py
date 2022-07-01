with open("input.txt", "r") as f:
    init_state = list(map(int, f.readline().split(',')))


def grow(init, days):
    states = {k: 0 for k in range(8, -1, -1)}
    for i in init:
        states[i] += 1
    for day in range(days):
        new_states = {k: 0 for k in range(8, -1, -1)}
        for k, v in states.items():
            if k != 0:
                new_states[k - 1] = v
            if k == 0 and v != 0:
                new_states[6] += max(v, 1)
                new_states[8] += max(v, 1)
        states = new_states
    return sum(states.values())


print(grow(init_state, 80))
print(grow(init_state, 256))
