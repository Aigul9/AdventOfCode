def part_1(nums):
    for i in range(25, len(nums)):
        preamble = nums[i - 25: i]
        if not any((nums[i] - j) in preamble for j in preamble):
            return nums[i]
            

def part_2(nums):
    for i in range(0, len(nums)):
        i_sum = nums[i]
        sum_list = [nums[i]]
        for j in range(i + 1, len(nums)):
            i_sum += nums[j]
            sum_list.append(nums[j])
            if i_sum == target:
                return sum_list
            if i_sum > target:
                break


with open('preamble.txt', 'r') as f:
    numbers = [int(line) for line in f.readlines()]

target = part_1(numbers)
print(target)
sums = part_2(numbers)
print(min(sums) + max(sums))
