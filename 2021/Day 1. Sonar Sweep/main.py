with open("input.txt", "r") as f:
    depth_list = [int(line.rstrip('\n')) for line in f]

count = 0
for i in range(1, len(depth_list)):
    if depth_list[i] > depth_list[i-1]:
        count += 1

print(count)

count3 = 0
for i in range(3, len(depth_list)):
    if depth_list[i] > depth_list[i-3]:
        count3 += 1

print(count3)
