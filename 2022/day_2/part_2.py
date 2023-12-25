def check_outcome(opponent_shape, player_shape):
    if (opponent_shape == player_shape - 1) or (player_shape == opponent_shape - 2):
        outcome = outcomes['Z']
    elif player_shape == opponent_shape:
        outcome = outcomes['Y']
    else:
        outcome = outcomes['X']

    return outcome

def outcome_points(play, player_shape):
    opponent_shape = play[0]

    # Convert the opponent's shape into a number
    opponent_shapes = {'A':1, 'B':2, 'C':3}
    opponent_shape = opponent_shapes[opponent_shape]

    if (opponent_shape == player_shape - 1) or (player_shape == opponent_shape - 2):
        outcome_points = 6
    elif player_shape == opponent_shape:
        outcome_points = 3
    else:
        outcome_points = 0
    return outcome_points

# Read in the file input
with open('data.txt', 'r') as f:
    data = f.read().splitlines()

# Split up each row into a list of two strings
for idx, row in enumerate(data):
    data[idx] = row.split()

total_score = 0
outcomes = {'X':'lose', 'Y':'draw', 'Z':'win'}
opponent_shapes = {'A':1, 'B':2, 'C':3}
player_shapes = [1, 2, 3]
for play in data:
    opponent_shape = opponent_shapes[play[0]]
    desired_outcome = outcomes[play[1]]
    for player_shape in player_shapes:
        if desired_outcome == check_outcome(opponent_shape, player_shape):
            shape_score = player_shape
            outcome_score = outcome_points(play, player_shape)
            total_score += (shape_score + outcome_score)
print(total_score)

