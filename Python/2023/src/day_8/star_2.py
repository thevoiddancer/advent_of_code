data = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


from itertools import cycle
from math import gcd

def lcd(a, b):
    return a * b // gcd(a, b)

def lcd_list(*args):
    if len(args) == 2:
        return lcd(args[0], args[1])
    else:
        return lcd_list(lcd(args[0], args[1]), *args[2:])
    
ins, _, *data = data.splitlines()
node_list = {k: v[1:-1].split(', ') for node in data for k, v in [node.split(' = ')]}

start_nodes = {idx: node for idx, node in enumerate([node for node in node_list if node[-1] == 'A'])}
periods = {idx: 0 for idx, _ in enumerate(start_nodes)}
turn_map = {'L': 0, 'R': 1}
# print(start_nodes)
# print(periods)

nodes = start_nodes.copy()
steps = 0
for instruction in cycle(ins):
    if all([per != 0 for per in periods]) or not nodes:
        break
    if any([node[-1] == 'Z' for node in nodes.values()]):
        cycled = [k for k, v in nodes.items() if v[-1] == 'Z']
        for cy in cycled:
            periods[cy] = steps
            del nodes[cy]
        # print(steps)
        # print(nodes)
    for idx, node in nodes.items():
        nodes[idx] = node_list[node][turn_map[instruction]]
    steps += 1
    
print(lcd_list(*periods.values()))