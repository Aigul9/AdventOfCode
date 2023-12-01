nums = [2, 0, 1, 7, 4, 14, 18]
nums_dict = {num: index for index, num in enumerate(nums, 1)}
next_num = nums[-1]
for i in range(len(nums), 2020):
    nums_dict[next_num], next_num = i, i - nums_dict.get(next_num, i)

print(next_num)

