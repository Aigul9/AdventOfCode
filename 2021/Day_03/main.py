with open("input.txt", "r") as f:
    numbers = [line.rstrip('\n') for line in f]


def convert_to_dec(num):
    return int(num, 2)


def part1():
    gamma = ''
    epsilon = ''
    numbers_len = len(numbers)
    for j in range(len(numbers[0])):
        count1 = len([num[j] for num in numbers if num[j] == '1'])
        count0 = numbers_len - count1
        if count1 > count0:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return convert_to_dec(gamma) * convert_to_dec(epsilon)


def get_list(param_name):
    param = ''
    param_list = numbers
    param_dict = {
        'oxygen': ['1', '0'],
        'co2': ['0', '1']
    }

    for j in range(len(numbers[0])):
        count1 = len([num[j] for num in param_list if num[j] == '1'])
        count0 = len(param_list) - count1
        if count1 >= count0:
            param += param_dict[param_name][0]
        elif count1 < count0:
            param += param_dict[param_name][1]
        param_list = [num for num in param_list if num[:j+1] == param]
        if len(param_list) == 1:
            break
    return param_list[0]


def part2():
    return convert_to_dec(get_list('oxygen')) * convert_to_dec(get_list('co2'))


print(part1())
print(part2())
