data = """#.#.....#.##.##.#
#.#.....#.##.##.#
.....#...#####...
...#.###....#...#
.###..####.#..#.#
#.###.#.#..###..#
..####...##.#.##.
..####...##.#.##.
#.#.#.#.#..###..#
.###..####.#..#.#
...#.###....#...#
.....#...#####...
#.#.....#.##.##.#"""


def find_smudge_hor(block, tposed):
    block = block.splitlines()
    for idx, _ in enumerate(block[:-1]):
        flipped = zip(block[: idx + 1][::-1], block[idx + 1 :])

        diffs = [[0 if a == b else 1 for a, b in zip(a, b)] for a, b in flipped]
        sum_diffs = sum([sum(d) for d in diffs])
        if sum_diffs == 1:
            x, y = [
                (c, r)
                for c, row in enumerate(diffs)
                for r, val in enumerate(row)
                if val == 1
            ][0]
            x = idx - x
            if tposed:
                x, y = y, x
            return (x, y)


def find_smudge(block):
    hor = find_smudge_hor(block, tposed=False)
    block = transpose(block)
    ver = find_smudge_hor(block, tposed=True)
    return hor or ver


def clean_smudge(block):
    sm_x, sm_y = find_smudge(block)
    block = [list(row) for row in block.splitlines()]
    block[sm_x][sm_y] = FLIP[block[sm_x][sm_y]]
    block = "\n".join(["".join(row) for row in block])
    return block, (sm_x, sm_y)


def find_axis_hor(block):
    block = block.splitlines()
    axes = []
    for idx, _ in enumerate(block[:-1]):
        flipped = zip(block[: idx + 1][::-1], block[idx + 1 :])
        if all([a == b for a, b in flipped]):
            axes.append(idx + 1)
    return axes


def find_axis(block):
    hor = find_axis_hor(block)
    block = transpose(block)
    ver = find_axis_hor(block)
    return {"hor": hor, "ver": ver}


def mirror_score(scores):
    rows = sum([row * 100 for row in scores["hor"]])
    cols = sum([col for col in scores["ver"]])
    return rows + cols


FLIP = {"#": ".", ".": "#"}

data = data.split("\n\n")
print(data)

scores = []
for idx, block in enumerate(data):
    # print(block)
    print()
    axis_old = find_axis(block)
    block, smudge = clean_smudge(block)
    axis_new = find_axis(block)
    axis_diff = {key: set(axis_new[key]) - set(axis_old[key]) for key in axis_new}
    score = mirror_score(axis_diff)
    scores.append(score)
    print("idx:", idx)
    print("old:", axis_old)
    print("smudge:", smudge)
    print("new:", axis_new)
    print("diff:", axis_diff)
    print("score:", score)
    print("\n\n")


print(scores)
print(sum(scores))