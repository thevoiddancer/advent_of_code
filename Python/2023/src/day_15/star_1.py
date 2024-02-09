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


def transpose(table):
    table = table.splitlines()
    data_T = [[table[i][j] for i in range(len(table))] for j in range(len(table[0]))]
    data_T = ["".join(line) for line in data_T]
    return "\n".join(data_T)


def sort_line(line):
    sorted_line = []
    for section in line.split("#"):
        sorted_line.append("".join(sorted(section)[::-1]))
    return "#".join(sorted_line)


data = transpose(data)

sorted_data = []
for line in data.splitlines():
    sorted_data.append(sort_line(line))

data = "\n".join(sorted_data)
data = transpose(data)
data = data.splitlines()
height = len(data)
weight = 0
for line in data:
    weight += line.count("O") * height
    height -= 1

print(weight)