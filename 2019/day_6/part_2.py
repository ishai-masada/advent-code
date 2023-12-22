"""
Day 6 Part 2
"""

# Read in data
with open('data.txt', 'r') as f:
    orbits = f.read().splitlines()

# Store the data with the key being the body orbiting the body as the value
orbits = {body.split(')')[1]: body.split(')')[0] for body in orbits if body}

'''
Function
yada yada yada
'''
def find_upwards_path(orbit_keys, orbit_values, end_orbit, above_orbit, current_idx):
    above_orbit = orbit_values[orbit_values.index(start_orbit) + 1]
    try:
        above_orbit = orbit_values[current_idx + 1]
        if above_orbit == end_orbit:
            return above_orbit
        else:
            find_upwards_path(orbit_keys, orbit_values, end_orbit, above_orbit, current_idx + 1)
    except IndexError:
        return None

start_orbit = orbits.get("YOU")
end_orbit = orbits.get("SAN")
orbit_keys = list(orbits.keys())
orbit_values = list(orbits.values())
print(orbit_values)

# Infinite Loop
while True:
    # End the loop if the current body is orbiting COM or the same body that SAN is orbiting
    if start_orbit == end_orbit or start_orbit == 'COM':
        break

    # Update the current body for each transfer
    start_orbit = orbits.get(start_orbit)

    # Find the index of the current body in the list of bodies orbiting the keys
    current_idx = orbit_values.index(start_orbit)
    print(f'{start_orbit}: {current_idx}')

    # Find the body in the orbit above the current body
    above_orbit = orbit_values[current_idx + 1]
    
    # Check if the current body is in the highest orbit
    if above_orbit != None:
        if find_upwards_path(orbit_keys, orbit_values, end_orbit, above_orbit, current_idx) == end_orbit:
            break
