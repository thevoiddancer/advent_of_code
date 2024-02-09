from rich import print as rprint
import re

data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

def transpose(table):
    data_T = [[table[i][j] for i in range(len(table))] for j in range(len(table[0]))]
    data_T = [''.join(line) for line in data_T]
    return data_T

def double_lines(table):
    double_rows = [idx for idx, line in enumerate(table) if '#' not in line]
    for row in double_rows[::-1]:
        table.insert(row, data[row])
    return table

def square_dist(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

data = data.splitlines()
data = double_lines(data)
HEIGHT = len(data)
data = transpose(data)
data = double_lines(data)
WIDTH = len(data)
data = transpose(data)

data_str = ''.join(data)
hash_patt = re.compile(r'#')
hash_find = hash_patt.finditer(data_str)
hash_locs = [m.start() for m in hash_find]

hash_locs = [divmod(loc, WIDTH) for loc in hash_locs]
# rprint('\n'.join(data))
# print(hash_locs)
distances = []
for idx, loc_a in enumerate(hash_locs[:-1]):
    for loc_b in hash_locs[idx + 1:]:
        distances.append(square_dist(loc_a, loc_b))
print(sum(distances))

# print(hash_locs[4], hash_locs[8], square_dist(hash_locs[4], hash_locs[8]))
# print(hash_locs[0], hash_locs[6], square_dist(hash_locs[0], hash_locs[6]))
# print(hash_locs[2], hash_locs[5], square_dist(hash_locs[2], hash_locs[5]))
# print(hash_locs[7], hash_locs[8], square_dist(hash_locs[7], hash_locs[8]))
