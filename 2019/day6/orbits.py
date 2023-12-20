orbits = '''
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN'''

#with open('input.txt', 'r') as g:
#    orbits = g.read()

orbits = {body.split(')')[1]: body.split(')')[0] for body in orbits.splitlines() if body}

def part_one(orbits):
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

def part_two(orbits):

    def find_upwards_path(orbits, end_orbit, above_orbit, current_index):
        above_orbit = list(orbits.values())[list(orbits.values()).index(current_body) + 1]
        # print(above_orbit)
        try:
            above_orbit = list(orbits.keys())[current_index + 1]
            if above_orbit == end_orbit:
                return above_orbit
            else:
                find_upwards_path(orbits, end_orbit, above_orbit, current_index + 1)
        except IndexError:
            return None

    start_orbit = orbits.get("YOU")
    end_orbit = orbits.get("SAN")
    current_body = start_orbit
    print(orbits)
    orbit_keys = list(orbits.keys())
    print(orbit_keys)
    orbit_values = list(orbits.values())
    print(orbit_values)
    while True:
        # print(current_body)
        if current_body == end_orbit or current_body == 'COM':
            break
        current_body = orbits.get(current_body)
        current_index = orbit_values.index(current_body)
        above_orbit = orbit_values[current_index + 1]
        print(above_orbit, current_index + 1, current_body)
        if above_orbit != None:
            if find_upwards_path(orbits, end_orbit, above_orbit, current_index) == end_orbit:
                break


part_two(orbits)

