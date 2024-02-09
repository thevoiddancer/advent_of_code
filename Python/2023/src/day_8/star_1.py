data = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

from rich import print as rprint
from itertools import cycle
ins, _, *nodes = data.splitlines()
data = {key.strip(): val.strip()[1:-1].split(', ') for key, val in [node.split('=') for node in nodes]}
# rprint(data)
turn = {'L': 0, 'R': 1}

start = 'AAA'
steps = 0
for direction in cycle(ins):
    # print(start)
    if start == 'ZZZ':
        break
    else:
        start = data[start][turn[direction]]
        steps += 1
print(steps)