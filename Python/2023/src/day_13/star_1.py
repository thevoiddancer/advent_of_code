from rich import print as rprint


def transpose(table):
    data_T = [[table[i][j] for i in range(len(table))] for j in range(len(table[0]))]
    data_T = ["".join(line) for line in data_T]
    return data_T


data = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def check_mirror(table, idx):
    flipped = zip(table[0 : idx + 1][::-1], table[idx + 1 :])
    mirrored = True
    for pre, post in flipped:
        if pre != post:
            mirrored = False
            break
    return mirrored


def mirrored_line(table):
    for idx, hor_line in enumerate(table[:-1]):
        if hor_line == table[idx + 1]:
            if check_mirror(table, idx):
                return idx + 1
    return 0


def mirrored_score(table):
    # horizontal
    hor = mirrored_line(table)
    table = transpose(table)
    ver = mirrored_line(table)
    return ver + 100 * hor


data = data.split("\n\n")

scores = []
for block in data:
    block = block.splitlines()
    scores.append(mirrored_score(block))

sum(scores)