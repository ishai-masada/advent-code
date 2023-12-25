with open("data.txt", 'r') as f:
    data = f.read().splitlines()

priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
total_priority = 0
for pack in data:
    compartment_1 = set(pack[:int(len(pack) / 2)])
    compartment_2 = set(pack[int(len(pack) / 2):len(pack)])
    common_letter = compartment_1.intersection(compartment_2)
    common_letter = ''.join(list(common_letter))
    total_priority += (priorities.find(common_letter) + 1)

print(total_priority)
