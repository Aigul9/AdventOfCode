with open("input.txt", "r") as f:
    numbers_list = [int(num) for num in f.readline().split(',')]

    boards_init = [line.rstrip('\n\n') for line in f]
    boards_dict = {}
    last_board = -1
    for i in range(len(boards_init)):
        if boards_init[i] == '':
            last_board += 1
            boards_dict[last_board] = []
        else:
            boards_dict[last_board].append([int(num) for num in boards_init[i].split()])


def get_winning_board(boards, is_part_one):
    winning_boards = []
    current_last_num = 0
    for num in numbers_list:
        for k, board in boards.items():
            for row in board:
                for idx in range(len(row)):
                    if row[idx] == num and k not in winning_boards:
                        row[idx] = -1
                        if sum(row) == -5 or sum([n[idx] for n in board]) == -5:
                            if is_part_one:
                                return boards[k], num
                            winning_boards.append(k)
                            current_last_num = num
    return boards[winning_boards[len(winning_boards) - 1]], current_last_num


def count_sum(board, num):
    return sum([num for row in board for num in row if num != -1]) * num


winning_board, last_num = get_winning_board(boards_dict, True)
print(count_sum(winning_board, last_num))
winning_board, last_num = get_winning_board(boards_dict, False)
print(count_sum(winning_board, last_num))
