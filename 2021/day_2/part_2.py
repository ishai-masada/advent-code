def part_two(directions):

    def depth(horizontal_position, aim, value, direction, depth):
        print(f'direction: {direction}')
        if direction == 'up':
            aim += value
        else:
            aim -= value

    def add_horizontal(horizontal_position, aim, value, direction, depth):
        horizontal_position += value
        depth += (aim*value)

    groups = re.findall(r'(\w+) (\d)', directions)

    commands = {'up': depth, 'forward': add_horizontal, 'down': depth}
    depth = 0
    horizontal_position = 0
    aim = 0

    for group in groups:
        direction, value = group[0], int(group[1])
        print(f'\nhorizontal_position: {horizontal_position}')
        print(f'depth: {depth}')
        print(f'aim: {aim}')
        print(f'direction: {direction}')
        print(f'value: {value}')
        commands.get(direction)(horizontal_position, aim, value, direction, depth)

    product = abs(depth)*horizontal_position
    print(product)
