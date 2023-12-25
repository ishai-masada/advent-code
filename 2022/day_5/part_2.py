# import data from text file
with open("data.txt", "r") as f:
    raw_data = f.read().splitlines()

# Extract rows, column numbers, and instructions
for idx, row in enumerate(raw_data):
    if len(row) == 0:
        stack_rows = raw_data[0:idx-1]
        column_num_row = raw_data[idx-1]
        raw_instructions = raw_data[idx + 1:len(raw_data)]

# Initialize dictionary with keys as column number and values as list of stacks
column_nums = list(map(int, column_num_row.split()))
list_of_lists = [list() for num in column_nums]
ordered_stacks = dict(zip(column_nums, list_of_lists))

# Format stacks in the dictionary
for row in stack_rows:
    stacks_in_row = row.split()
    counted_stacks = []
    for stack in stacks_in_row:

        # Check if the stack has already been added to the dictionary
        if stack[1] in counted_stacks:
            continue

        # Find The horizontal position of each stack in its respective row
        matches = [idx for idx, letter in enumerate(row) if letter == stack[1]]
        
        # Add the stack to the list to show that it has been added to the dictionary already
        counted_stacks.append(stack[1])
        
        # Add stack to dictionary for every instance in the same row
        for idx in matches:
            stack_column = int(column_num_row[idx])

            # Add the stack to the dictionary using the column number
            ordered_stacks.get(stack_column).append(stack)

# Initialize list for numbers that represent the instructions
instructions = []

# Extract the numbers from the raw instructions
for row in raw_instructions:
    nums = [int(word) for word in row.split() if word.isdigit()]
    instructions.append(nums)

# Move the stacks according to the instructions
for instruction in instructions:
    for idx in range(instruction[0] - 1, -1, -1):
        ordered_stacks.get(instruction[2]).insert(0, ordered_stacks.get(instruction[1]).pop(idx))

# Put the letters of each stack together into one string
answer_string = ''
for column in ordered_stacks.values():
    answer_string += column[0][1]

print(answer_string)
