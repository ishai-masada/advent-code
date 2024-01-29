with open("data.txt", 'r') as f:
    data = f.read().splitlines()

priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
total_priority = 0
for pack in data[::3]:
    group = data[data.index(pack): data.index(pack) + 3]
    common_letter = set(group[0]).intersection(set(group[1]), set(group[2]))
    common_letter = ''.join(list(common_letter))
    total_priority += (priorities.find(common_letter) + 1)

print(total_priority)
