from rich import print as rprint

data = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

_data = """
.....
.....
.....
...#.
.....
"""
import functools


# @functools.cache
# def transpose(table):
#     table = table.splitlines()
#     data_T = [[table[i][j] for i in range(len(table))] for j in range(len(table[0]))]
#     data_T = ["".join(line) for line in data_T]
#     return "\n".join(data_T)


# @functools.cache
# def sort_line(line):
#     sorted_line = []
#     for section in line.split("#"):
#         sorted_line.append("".join(sorted(section)[::-1]))
#     return "#".join(sorted_line)


# @functools.cache
# def align_Os(block):
#     sorted_data = []
#     for line in block.splitlines():
#         sorted_data.append(sort_line(line))
#     return "\n".join(sorted_data)


# @functools.cache
# def rotate_block(block):
#     height = len(block.splitlines())
#     width = len(block.splitlines()[0])
#     block = block.splitlines()
#     block = "\n".join(
#         ["".join([block[i][j] for i in range(height)]) for j in range(width)][::-1]
#     )
#     return block


@functools.cache
def calculate_weight(block):
    block = block.splitlines()
    height = len(block)
    weight = 0
    for line in block:
        weight += line.count("O") * height
        height -= 1
    return weight


@functools.cache
def sort_hor(block, west):
    y = []
    for line in block.splitlines():
        sorted_line = []
        for segment in line.split("#"):
            sorted_line.append("".join(sorted(segment, reverse=west)))
        sorted_line = "#".join(sorted_line)
        y.append("".join(sorted_line))
    block = "\n".join(y)
    return block


@functools.cache
def sort_ver(block, north):
    block = [list(block) for block in block.splitlines()]
    height = len(block)
    width = len(block[0])
    for idy in range(width):
        col = "".join([block[idx][idy] for idx in range(height)])
        sorted_col = []
        for segment in col.split("#"):
            sorted_col.append("".join(sorted(segment, reverse=north)))
        col = "#".join(sorted_col)
        for idx in range(height):
            block[idx][idy] = col[idx]

    block = "\n".join(["".join(row) for row in block])
    return block


ROTATION = "north west south east".split()
ROTATION_MAP = {
    "west": (sort_hor, True),
    "east": (sort_hor, False),
    "north": (sort_ver, True),
    "south": (sort_ver, False),
}


@functools.cache
def cycle(block):
    for rot in ROTATION:
        fun, arg = ROTATION_MAP[rot]
        block = fun(block, arg)
    return block


seen = []
repeat = []
cycle_lenght = 0
total_cycles = 1000000000
for i in range(total_cycles):
    data = cycle(data)
    h = hash(data)
    if h not in seen:
        seen.append(h)
    else:
        if h not in repeat:
            repeat.append(h)
            cycle_lenght += 1
        else:
            break

print(i)
first = seen.index(repeat[0])
resto = (total_cycles - first) % cycle_lenght
print(resto)
for i in range(resto - 1):
    data = cycle(data)
print(calculate_weight(data))
