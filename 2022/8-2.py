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
example_trans = list(zip(*example))

height = len(example)
width = len(example[0])

def check_height(h, l):
    see = 0
    obstructed = False
    for value in l:
        if obstructed:
            break
        elif value < h:
            see += 1
        else:
            see += 1
            obstructed = True
    return see


def check_spot(r, c):
    vis_l = check_height(example[r][c], example[r][:c][::-1])
    vis_r = check_height(example[r][c], example[r][:c:-1][::-1])
    vis_t = check_height(example[r][c], example_trans[c][:r][::-1])
    vis_b = check_height(example[r][c], example_trans[c][:r:-1][::-1])
    return vis_l * vis_r * vis_t * vis_b


M = 0
for row in range(1, height):
    for column in range(1, width):
        if check_spot(row, column) > M:
            M = check_spot(row, column)
            r, c = row, column

print()