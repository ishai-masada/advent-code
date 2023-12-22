'''
Day 6 Part 1
'''

# Read in data
with open('data.txt', 'r') as f:
    orbits = f.read()

# Store the data with label being the body orbiting the body as the value
orbits = {body.split(')')[1]: body.split(')')[0] for body in orbits.splitlines() if body}

indirect_orbits = 0

# Iterate through each body
for body in orbits:
    bah = 0
    # Find every body that 
    while True:
        body = orbits.get(body)
        if body == 'COM':
            break
        indirect_orbits += 1

direct_orbits = len(orbits)
answer = indirect_orbits + direct_orbits
print(answer)
