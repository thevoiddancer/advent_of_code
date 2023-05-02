example = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

with open('9.txt', 'r') as file:
    data = file.read()

data = iter(data.splitlines())


def sign(x):
    return int(x / abs(x)) if x else 0


def direction(x):
    dir_dict = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }
    return dir_dict[x]


class Knot:
    """
    Class for holding knot information such as name, coordinates and movement methods.
    """

    def __init__(self, name=None, loc=(0, 0)):
        self.name = name
        self.loc = loc
        self._unpack_loc()

    def _unpack_loc(self):
        self.x = self.loc[0]
        self.y = self.loc[1]

    def __repr__(self):
        return f"{(self.name + ': ') if self.name else ''}{self.loc}"

    def distance(self, other):
        d = ((other.x - self.x), (other.y - self.y))
        return d

    def step(self, other):
        d = self.distance(other)
        step = tuple(sign(coord) for coord in d)
        return step

    def move(self, step):
        self.loc = tuple(s + o for s, o in zip(self.loc, step))
        self._unpack_loc()

    def move_toward(self, other):
        self.move(self.step(other))
        self._unpack_loc()

    def touching(self, other):
        return not (max(self.distance(other)) > 1 or min(self.distance(other)) < -1)


def draw_grid():
    offset = 0
    n = max([i for step in trail for i in step] if trail else [0]) + 2 + offset
    grid = [['.' for _ in range(n)] for _ in range(n)]
    grid[0 + offset][0 + offset] = 'S'
    for (x, y) in trail:
        grid[y + offset][x + offset] = '#'
    grid = '\n'.join(''.join(line) for line in grid[::-1])
    print(grid)
    return


def trace_tail():
    offset = -min([i for step in trail for i in step])
    n = max([i for step in trail for i in step] if trail else [0]) + 2 + offset

    grid = [['.' for _ in range(n)] for _ in range(n)]
    for (x, y) in trail:
        grid[y + offset][x + offset] = '#'

    grid = '\n'.join(''.join(line) for line in grid[::-1])
    print(grid)
    return


def move_snake():
    move = next(data)
    to, steps = move.split()
    to = direction(to)
    for _ in range(int(steps)):
        body[0].move(to)
        for seg, prev in zip(body[1:], body[:-1]):
            if not seg.touching(prev):
                seg.move_toward(prev)
        if body[-1].loc not in trail:
            trail.add(body[-1].loc)


body = [Knot(str(i)) for i in range(10)]
body[0] = Knot('H')
trail = set()

while data:
    try:
        move_snake()
    except Exception:
        break


print(len(trail))
