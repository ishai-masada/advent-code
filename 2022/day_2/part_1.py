# Function for determining the results of each round 
def outcome(play, player_shape):
    opponent_shape = play[0]

    # Convert the opponent's shape into a number
    opponent_shapes = {'A':1, 'B':2, 'C':3}
    opponent_shape = opponent_shapes[opponent_shape]

    if (opponent_shape == player_shape - 1) or (player_shape == opponent_shape - 2):
        outcome = 6
    elif player_shape == opponent_shape:
        outcome = 3
    else:
        outcome = 0
    return outcome

# Read in the file input
with open('data.txt', 'r') as f:
    data = f.read().splitlines()

# Split up each row into a list of two strings
for idx, row in enumerate(data):
    data[idx] = row.split()

total_score = 0
for play in data:
    opponent_shape = play[0]
    player_shape = play[1]
    player_shapes = {'X':1, 'Y':2, 'Z':3}

    # Convert your shape into a number
    player_shape = player_shapes[player_shape]

    outcome_points = outcome(play, player_shape)
    shape_points = player_shape
    round_score = shape_points + outcome_points
    total_score += round_score
print(total_score)
