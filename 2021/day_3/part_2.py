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

bin_nums = re.findall(r'(\d+)', bin_nums)
digits = []
nums = []

for _ in range(0, len(bin_nums[0])):
    digits.append([])

for num in bin_nums:
    for idx, digit in enumerate(digits):
        digit.append(num[idx])

for digit in digits:
    if len(bin_nums) == 1:
        break
    count = 0

    # If the number of 1s and 0s are equal, keep the numbers with a 1 in the current position
    elif digit.count('1') == digit.count('0'):
        for idx, num in enumerate(bin_nums):
            if num[idx-count] != 1:
                bin_nums.remove(num)
            count += 1

    # If the number of 1s is greater than the number of 0s, keep the numbers with a 1 in
    # the current position
    elif digit.count('1') > digit.count('0'):
        for idx, num in enumerate(bin_nums):
            if num[idx-count] != 1:
                bin_nums.remove(num)
            count += 1

    # If the number of 1s is less than the number of 0s, keep the numbers with a 0 in
    # the current position
    elif digit.count('1') < digit.count('0'):
        for idx, num in enumerate(bin_nums):
            if num[idx-count] != 0:
                bin_nums.remove(num)
            count += 1

print(int(bin_nums[0], 2))
# print(life_supporter_rating)
