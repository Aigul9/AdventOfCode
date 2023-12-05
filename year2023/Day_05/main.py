from utils.measure import timeit, memory


def get_mapped_values(input_list, prev_value):
    dst, src, rng = [int(i) for i in input_list.split()]
    if src <= prev_value < src + rng:
        return dst + (prev_value - src)


def part1(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n\n')
        _, seeds = lines[0].split('seeds: ')
        seeds = list(seeds.split())
        seeds_dict = {int(key): int(key) for key in seeds}
        for line in lines:
            map_values = line.split('\n')[1:]
            for key, value in seeds_dict.items():
                for row in map_values:
                    new_dst = get_mapped_values(row, value)
                    if new_dst:
                        seeds_dict[key] = get_mapped_values(row, value)
                        break

        return min(v for v in seeds_dict.values())


if __name__ == '__main__':
    assert part1('test.txt') == 35
    print(part1('input.txt'))
