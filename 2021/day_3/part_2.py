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

def o2(digits, bin_nums):
    for idx, digit in enumerate(digits):

        if len(bin_nums) == 1:
            break

        # If the number of 1s is greater than the number of 0s, keep the numbers with a 1 in
        # the current position
        elif digit.count('1') > digit.count('0'):
            bin_nums = [num for num in bin_nums if num[idx] == '1']
            digit.remove('0')

        elif digit.count('1') < digit.count('0'):
            bin_nums = [num for num in bin_nums if num[idx] == '0']
            digit.remove('1')

        elif digit.count('1') == digit.count('0'):
            bin_nums = [num for num in bin_nums if num[idx] == '1']
            digit.remove('0')


    o2 = int(bin_nums[0], 2)
    print(o2)
    return o2


def co2():
    for idx, digit in enumerate(digits):

        if len(bin_nums) == 1:
            break

        # If the number of 1s is greater than the number of 0s, keep the numbers with a 1 in
        # the current position
        elif digit.count('1') < digit.count('0'):
            bin_nums = [num for num in bin_nums if num[idx] == '1']

        elif digit.count('1') == digit.count('0'):
            bin_nums = [num for num in bin_nums if num[idx] == '0']

        elif digit.count('1') > digit.count('0'):
            bin_nums = [num for num in bin_nums if num[idx] == '0']

    co2 = int(bin_nums[0], 2)
    print(co2)

    return co2

o2(digits, bin_nums)
# co2(digits, bin_nums)


# life_support_rating = co2*o2
# print(life_support_rating)
