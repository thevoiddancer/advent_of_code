from rich import print as rprint

data = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

from collections import defaultdict

HEIGHT = len(data.splitlines())
WIDTH = len(data.splitlines()[0])
data = {divmod(idx, WIDTH): val for idx, val in enumerate(data.replace("\n", ""))}
energized = defaultdict(lambda: ".")
seen_beams = []

beams = [{"loc": (0, -1), "dir": "E"}]
DIRECTION = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}


def move(location, direction):
    direction = DIRECTION[direction]
    destination = tuple(a + b for a, b in zip(location, direction))
    return destination


OBJECTS = {
    "|": {"N": ["S"], "S": ["N"], "E": ["N", "S"], "W": ["N", "S"]},
    "-": {"N": ["W", "E"], "S": ["W", "E"], "E": ["W"], "W": ["E"]},
    "/": {"N": ["W"], "S": ["E"], "E": ["S"], "W": ["N"]},
    "\\": {"N": ["E"], "S": ["W"], "E": ["N"], "W": ["S"]},
    ".": {"N": ["S"], "S": ["N"], "E": ["W"], "W": ["E"]},
}

OPPO = {"N": "S", "S": "N", "E": "W", "W": "E"}

# beams = [{'loc': (0, 1), 'dir': 'N'}, {'loc': (0, 1), 'dir': 'S'}]
# step = 0
while beams:
    # step += 1
    # if step == 40:
    #     break
    beam = beams.pop(0)
    # print(beam['loc'])
    if beam["loc"] != (0, -1):
        energized[beam["loc"]] = "#"
    if beam in seen_beams:
        continue
    seen_beams.append(beam)

    # print('beam', beam)
    next_loc = move(beam["loc"], beam["dir"])
    # print(next_loc)
    try:
        next_val = data[next_loc]
    except Exception:
        # print('OUT OF BOUNDS')
        # print()
        continue
    obj = OBJECTS[next_val]
    coming_from = OPPO[beam["dir"]]
    next_beams = [{"loc": next_loc, "dir": next_dir} for next_dir in obj[coming_from]]
    # print('NEXT:', next_loc, next_val, obj[coming_from])
    # print('next beams', next_beams)
    beams.extend(next_beams)
    # print('all beams', beams)
    # print('-------------------------------------------------------------')
print(len(dict(energized)))