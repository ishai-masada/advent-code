# Day 1 of Advent of Code 2022
with open('data.txt', 'r') as f:
    data = f.read().split('\n\n')

# Store the data in a list of lists that represent the calories
for idx, elem in enumerate(data):
    data[idx] = elem.split('\n')
    for i, string in enumerate(data[idx]):
        if len(string) > 0:
            data[idx][i] = int(string)
        else:
            data[idx].remove(string)

for idx, elf in enumerate(data):
    data[idx] = sum(elf)

total = 0

for i in range(3):
    total += max(data)
    data.remove(max(data))

print(total)

