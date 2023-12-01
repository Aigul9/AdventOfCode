import re


def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == '__main__':
    positions = []
    with open('test.txt', 'r') as f:
        for line in f.readlines():
            line = list(map(int, re.findall(f'-?\d+', line)))
            positions.append(line)

    y_target = 2000000
    x_list = []
    for position in positions:
        xs, ys, xb, yb = position
        dist = get_dist(xs, ys, xb, yb)
        y_start, y_end = ys - dist, ys + dist
        x_start, x_end = xs - dist, xs + dist
        if y_start <= y_target <= y_end:
            y_diff = abs(ys - y_target)
            x1, x2 = x_start + y_diff, x_end - y_diff
            if x1 < xb < x2 and yb == y_target:
                x_list.append([x1, xb - 1])
                x_list.append([xb + 1, x2])
            elif x1 == xb == x2:
                continue
            elif xb == x1:
                x_list.append([x1 + 1, x2])
            elif xb == x2:
                x_list.append([x1, x2 - 1])
            else:
                x_list.append([x1, x2])
    new_set = set()
    for li in x_list:
        new_set.update(range(li[0], li[1] + 1))
    print(len(new_set))
