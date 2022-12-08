import timeit


def fun(n):
    for i in range(n, len(line)):
        sub = line[i-n:i]
        if len(set(sub)) == len(sub):
            return i


start = timeit.default_timer()

tests = [
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb',  # 7
    'bvwbjplbgvbhsrlpgdmjqwftvncz',  # 5
    'nppdvjthqldpwncqszvftbrmjlhg',  # 6
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',  # 10,
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'  # 11
]

with open('input.txt', 'r') as f:
    line = f.read()

print(fun(4))
print(fun(14))

end = timeit.default_timer()
print(end - start)
