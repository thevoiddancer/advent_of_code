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

def expand_lines(table, expand_value):
    weights = [1 if '#' in line else expand_value for line in table]
    return weights

def square_dist(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def square_dist_weights(a, b):
    r_min = min(a[0], b[0])
    r_max = max(a[0], b[0])
    c_min = min(a[1], b[1])
    c_max = max(a[1], b[1])
    return sum(col_weights[c_min : c_max]) + sum(row_weights[r_min : r_max])

expand = 1e6
data = data.splitlines()
row_weights = expand_lines(data, expand)
HEIGHT = len(data)
data = transpose(data)
col_weights = expand_lines(data, expand)
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
        dist = square_dist_weights(loc_a, loc_b)
        distances.append(dist)
print(sum(distances))

# print(row_weights)
# print(col_weights)
# print(hash_locs)
# rprint(data)
# print(hash_locs[4], hash_locs[8], square_dist(hash_locs[4], hash_locs[8]))
# print(hash_locs[0], hash_locs[6], square_dist(hash_locs[0], hash_locs[6]))
# print(hash_locs[2], hash_locs[5], square_dist(hash_locs[2], hash_locs[5]))
# print(hash_locs[7], hash_locs[8], square_dist(hash_locs[7], hash_locs[8]))

# square_dist_weights((0, 3), (2, 0))