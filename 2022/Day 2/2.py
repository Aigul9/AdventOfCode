with open('2.txt', 'r') as f:
    lines = [line.strip().split() for line in f.readlines()]

opt_points = {
    'X': 1,  # A, X - rock - 1
    'Y': 2,  # B, Y - paper - 2
    'Z': 3,  # C, Z - scissors - 3
}

match_points = {
    'win': 6,
    'draw': 3,
    'loss': 0
}

# Rock defeats Scissors A > Z, X > C
# Scissors defeats Paper C > Y, Z > B
# Paper defeats Rock B > X, Y > A
win_options = ['AY', 'BZ', 'CX']
draw_options = ['AX', 'BY', 'CZ']
loss_options = ['AZ', 'BX', 'CY']

res = 0
for i, j in lines:
    joined = ''.join((i, j))
    if joined in win_options:
        res += match_points['win']
    elif joined in draw_options:
        res += match_points['draw']
    else:
        res += match_points['loss']
    res += opt_points[j]
print(res)

# X - loss
# Y - draw
# Z - win

res2 = 0
for i, j in lines:
    if j == 'X':
        opt = [o for o in loss_options if i in o][0][1]
        res2 += match_points['loss']
    elif j == 'Y':
        opt = [o for o in draw_options if i in o][0][1]
        res2 += match_points['draw']
    else:
        opt = [o for o in win_options if i in o][0][1]
        res2 += match_points['win']
    res2 += opt_points[opt]

print(res2)
