t = str.maketrans('FBLR', '0101')
with open('boards.txt', 'r') as f:
    boards = [int(line.strip().translate(t), 2) for line in f.readlines()]

print(max(boards))
boards.sort()
for i in range(1, len(boards)):
    if boards[i] - boards[i - 1] == 2:
        print(boards[i] - 1)
        break
