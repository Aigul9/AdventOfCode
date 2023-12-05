from utils.measure import timeit, memory


def get_mapped_values(input_list, seeds_input):
    dst, src, rng = [int(i) for i in input_list.split()]
    zipped = list(zip(range(dst, dst + rng), range(src, src + rng)))
    for key, value in seeds_input.items():
        res = [d for d, s in zipped if s == value]
        if res:
            seeds_input[key] = res[0]
    return seeds_input


def part1(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n\n')
        _, seeds = lines[0].split('seeds: ')
        seeds = list(seeds.split())
        seeds_dict = {int(key): int(key) for key in seeds}
        for line in lines:
            map_values = line.split('\n')[1:]
            for row in map_values:
                seeds_dict = get_mapped_values(row, seeds_dict)

        print(seeds_dict)


if __name__ == '__main__':
    # assert part1('test.txt') == 13
    print(part1('input.txt'))
