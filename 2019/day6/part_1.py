'''
Day 6 Part 1
'''

with open('data.txt', 'r') as f:
    orbits = f.read()

orbits = {body.split(')')[1]: body.split(')')[0] for body in orbits.splitlines() if body}

indirect_orbits = 0

for body in orbits:
    while True:
        body = orbits.get(body)
        if body == 'COM':
            break
        indirect_orbits += 1

direct_orbits = len(orbits)
answer = indirect_orbits + direct_orbits
print(answer)
