data = """.....
.S-7.
.|.|.
.L-J.
....."""

_data = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

_data = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

_data = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

def next_pipe(loc, prev = None):
    all_sides = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if data[loc] != 'S':
        connected_sides = DIRECTIONS[data[loc]]
    else:
        connected_sides = all_sides
    sides = set(all_sides) & set(connected_sides)
    neighbours = {tuple(map(sum, zip(loc, side))) for side in sides} - set([prev])
    # print(neighbours)
    # print('currpos:', data[loc])
    # print('prevpos:', prev)
    for neighbour in neighbours:
        # print('nextposs:', data[neighbour])
        if WIDTH >= neighbour[0] >= 0 and HEIGHT >= neighbour[1] >= 0 and data[neighbour] in DIRECTIONS:
            # print('viableposs:', data[neighbour])
            yield neighbour

def move(loc, step):
    return tuple(map(sum, zip(loc, step)))

DIRECTIONS = {
    '-': ((0, 1), (0, -1)),
    '|': ((1, 0), (-1, 0)),
    '7': ((1, 0), (0, -1)),
    'F': ((0, 1), (1, 0)),
    'L': ((0, 1), (-1, 0)),
    'J': ((-1, 0), (0, -1)),
}

WIDTH = len(data.splitlines()[0])
HEIGHT = len(data.splitlines())

start = data.find('S')
start = divmod(start, WIDTH + 1)

data = {divmod(loc, WIDTH): val for loc, val in enumerate(''.join(data.splitlines()))}



prev_locs = {'left': None, 'right': None}
# print('prev:', prev_locs)
curr_locs = {'left': start, 'right': start}
# print('curr:', curr_locs)
sides = {loc: [move(loc, step) for step in DIRECTIONS[data[loc]]] for loc in next_pipe(start)}
sides = {key: val for key, val in sides.items() if start in val}
next_locs = {side: pos for side, pos in zip(['left', 'right'], sides)}
# print('next:', next_locs)
step = 0
while not (len(set(curr_locs.values())) == 1 and all(prev_locs.values())):
    # print('---------')
    prev_locs = curr_locs.copy()
    # print('prev:', prev_locs)
    curr_locs = next_locs.copy()
    # print('curr:', curr_locs)
    next_locs = {side: next(next_pipe(pos, prev_locs[side])) for side, pos in curr_locs.items()}
    # print('next:', next_locs)
    step += 1

print(step)
