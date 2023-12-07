from collections import Counter


def part1(path):
    with open(path, 'r') as f:
        games = {}
        orders = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        ordering = {value: index for index, value in enumerate(orders)}

        for line in f.read().split('\n'):
            hand, bid = line.split()
            cards_dict = {char: hand.count(char) for char in set(hand)}
            cards_dict = dict(sorted(cards_dict.items(), key=lambda x: (-x[1], ordering[x[0]])))
            # print(cards_dict)
            keys = ''.join(str(key) for key in cards_dict.keys())
            values = ''.join(str(value) for value in cards_dict.values())
            games[(values, keys)] = int(bid)
            # print((values, keys))
        # for k, v in games.items():
        #     print(k[0])
        games = dict(sorted(games.items(), key=lambda x: (x[0][0], x[0][1])))
        print(games)
        # print(sum((i + 1) * value for i, value in enumerate(games.values())))
        # return sum((i + 1) * value for i, value in enumerate(games.values()))


if __name__ == '__main__':
    assert part1('test.txt') == 6440
    print(part1('input.txt'))
