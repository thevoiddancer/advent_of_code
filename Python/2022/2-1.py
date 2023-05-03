# Symbols
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

# Points
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

example = """A Y
B X
C Z
"""
#
# This strategy guide predicts and recommends the following:
#
#     In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
#     In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
#     The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
#
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
#
# What would your total score be if everything goes exactly according to your strategy guide?


def result(first, second):
    second = {'X': 'A', 'Y': 'B', 'Z': 'C'}[second]
    beats = {'A': 'C', 'B': 'A', 'C': 'B'}
    value = {'A': 1, 'B': 2, 'C': 3}
    if first == second:
        match = 3
    elif beats[second] == first:
        match = 6
    else:
        match = 0
    return match + value[second]

with open('2.txt', 'r') as file:
    print(sum([result(*pair.split()) for pair in file.read().split('\n')[:-1]]))
