# Day 3 | Part 1
# Submarine Status Repot
# Ishai Masada

import re

# with open('num_list.txt', 'r') as f:
#     bin_nums = f.read()

bin_nums = '''
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''

bin_nums = [num for num in bin_nums.splitlines() if num]
digits = []
nums = []

for _ in range(0, len(bin_nums[0])):
    digits.append([])

for num in bin_nums:
    for idx, digit in enumerate(digits):
        digit.append(num[idx])

# for count, digit in enumerate(digits):
#     if len(bin_nums) == 1:
#         break

#     most_comm = '1' if bin_nums.count('1') >= bin_nums.count('0') else '0'

#     for num in bin_nums:
#         print(f'{num=}, {count=}')
#         if num[count] != most_comm:
#             bin_nums.remove(num)

for count, digit in enumerate(digits):
    if len(bin_nums) == 1:
        break

    least_comm = '0'# if bin_nums.count('0') > bin_nums.count('1') else '1'
    print(f'{least_comm=}')

    for num in bin_nums:
        print(num)
        if num[count] != least_comm:
            bin_nums.remove(num)
    # print(bin_nums)

print(int(bin_nums[0], 2))
# print(life_supporter_rating)
