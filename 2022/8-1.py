from collections import defaultdict

example = """30373
25512
65332
33549
35390"""

with open('8.txt', 'r') as file:
    example = file.read()

# To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.
# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column;

example = [[int(i) for i in line] for line in example.splitlines()]

height = len(example)
width = len(example[0])


def check_height(row, column, vis, hid, reverse=True):
    line = example[row][:column + 1]
    tree = example[row][column]
    if tree == max(line) and line.count(tree) == 1:
        print(row, column, example[r][c], 'visible')
        vis += 1
    else:
        print(row, column, example[r][c], 'hidden')
        if reverse:
            column = len(example) - column - 1
        hid[row].append(column)
    return vis, hid


def print_grid():
    for line in example:
        print(line)


visible = 0
hidden = defaultdict(list)

# L2R
for r in range(1, len(example) - 1):
    for c in range(1, len(example[0]) - 1):
        visible, hidden = check_height(r, c, visible, hidden)
print_grid()
print(hidden)
print('visible:', visible)
print('--------------------------------------------')

# R2L
example = [row[::-1] for row in example]
hidden_old = hidden.copy()
hidden = defaultdict(list)
for r in range(1, len(example) - 1):
    for c in range(1, len(example[0]) - 1):
        if c in hidden_old[r]:
            visible, hidden = check_height(r, c, visible, hidden, reverse=False)
print_grid()
print(hidden)
print('visible:', visible)
print('--------------------------------------------')

### VERTICAL
# T2B
example = list(zip(*example))
hidden_old = hidden.copy()
hidden = defaultdict(list)
for r in range(1, len(example) - 1):
    for c in range(1, len(example[0]) - 1):
        if r in hidden_old[c]:
            visible, hidden = check_height(r, c, visible, hidden)
print_grid()
print(hidden)
print('visible:', visible)
print('--------------------------------------------')

#B2T

example = [row[::-1] for row in example]
hidden_old = hidden.copy()
hidden = defaultdict(list)
for r in range(1, len(example) - 1):
    for c in range(1, len(example[0]) - 1):
        if c in hidden_old[r]:
            visible, hidden = check_height(r, c, visible, hidden)
print_grid()
print(hidden)
print('visible:', visible)
print('--------------------------------------------')

visible = visible + 2 * height + 2 * (width - 2)
print(visible)