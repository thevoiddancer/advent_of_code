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


beams = [{"loc": (0, -1), "dir": "E"}]

def traverse_beams(beams):
    energized = defaultdict(lambda: ".")
    seen_beams = []
    while beams:
        beam = beams.pop(0)
        if beam["loc"] != (0, -1):
            energized[beam["loc"]] = "#"
        if beam in seen_beams:
            continue
        seen_beams.append(beam)

        next_loc = move(beam["loc"], beam["dir"])
        try:
            next_val = data[next_loc]
        except Exception:
            # print('OUT OF BOUNDS')
            # print()
            continue
        obj = OBJECTS[next_val]
        coming_from = OPPO[beam["dir"]]
        next_beams = [{"loc": next_loc, "dir": next_dir} for next_dir in obj[coming_from]]
        beams.extend(next_beams)

    return len(dict(energized)), list(energized.keys())

all_sources = (
    [{"loc": (-1, idx), "dir": "S"} for idx in range(WIDTH)]
    + [{"loc": (HEIGHT, idx), "dir": "N"} for idx in range(WIDTH)]
    + [{"loc": (idx, -1), "dir": "E"} for idx in range(HEIGHT)]
    + [{"loc": (idx, WIDTH), "dir": "W"} for idx in range(HEIGHT)]
)

_all_sources = [{'loc': (0, -1), 'dir': 'E'}]
results = []
list_of_energized = []
for source in all_sources:
    count, locs = traverse_beams([source])
    results.append(count)
    list_of_energized.append(locs)
max(results)