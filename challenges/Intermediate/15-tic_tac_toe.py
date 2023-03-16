# Tic Tac Toe
# Create a function that takes a list of character inputs from a Tic Tac Toe game. 
# Inputs will be taken from player1 as "X", player2 as "O", and empty spaces as "#". 
# The program will return the winner or tie results.

# Examples
# tic_tac_toe([
#   ["X", "O", "O"],
#   ["O", "X", "O"],
#   ["O", "#", "X"]
# ]) ➞ "Player 1 wins"


# tic_tac_toe([
#   ["X", "O", "O"],
#   ["O", "X", "O"],
#   ["X", "#", "O"]
# ]) ➞ "Player 2 wins"


# tic_tac_toe([
#   ["X", "X", "O"],
#   ["O", "X", "O"],
#   ["X", "O", "#"]
# ]) ➞ "It's a Tie"

# Notes
# All inputs are valid (there will be no games where both players win).

def tic_tac_toe(inputs):

    # add options to win in row
    options = inputs 

    # add options to win in columns 
    inv = [["#","#","#"],
           ["#","#","#"],
           ["#","#","#"]]

    for r in range(0,3):  
        for c in range(0,3):
            inv[r][c]=inputs[c][r]

    options = options + inv

    # add options to win in diagonal
    options.append([inputs[0][0],inputs[1][1],inputs[2][2]])
    options.append([inputs[2][0],inputs[1][1],inputs[0][2]])

    
    for row in options:
        
        if row.count("X") == 3: 
            return "Player 1 wins"

        if row.count("O") == 3:
            return "Player 2 wins"
  
    return "It's a Tie"



print(tic_tac_toe([
  ["X", "X", "O"],
  ["X", "O", "O"],
  ["X", "O", "#"]
]))