def run():
    with open('input.txt', 'r') as f:
        lines = f.read().split('\n')
        total = 0
        digit_dict = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }

        for line in lines:
            print(line)
            new_line = ''
            for char in line:
                new_line += char
                for k, v in digit_dict.items():
                    if k in new_line:
                        new_line = new_line.replace(k, v)
            # for k, v in digit_dict.items():
            #     line = line.replace(k, v)
            digits = ''.join([char for char in new_line if char.isdigit()])
            print(new_line)
            # print(digits)
            total += int(f'{digits[0]}{digits[-1]}')
            print(f'{digits[0]}{digits[-1]}')
        print(total)


if __name__ == '__main__':
    run()
