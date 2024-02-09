data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

import re
from operator import add
from itertools import product
from rich import print as rprint
from math import prod
width = len(data.splitlines()[1])
side = [-1, 0, 1]
neighbours = [prod for prod in product(side, side) if prod != (0, 0)]

# Get numbers out as {num: [locations]}

pattern_nums = re.compile(r'(\d+)')
parts_per_location = {}
for row, line in enumerate(data.splitlines()):
    groups = re.finditer(pattern_nums, line)
    for group in groups:
        start = group.start()
        end = group.end()
        num = int(group.group())
        for col in range(start, end):
            parts_per_location[(row, col)] = {'value': num, 'locs':[(row, col_) for col_ in range(start, end)]}
# rprint(parts_per_location)
parts_per_location_backup = parts_per_location.copy()

# Get all connecting characters > all are captured
pattern_conn = re.compile(r'[^0-9\.\n]')
connections = re.finditer(pattern_conn, data)
connection_locations = {}
for conn in connections:
    if conn.group() == "*":
        location = divmod(conn.start(), width+1)
        connection_locations[location] = conn.group()

# rprint(connection_locations)
# Remove parts that are connected
total = 0
for location in connection_locations:
    connected_parts = []
    for step in neighbours:
        neighbour = tuple(map(add, location, step))
        if neighbour in parts_per_location:
            connected_parts.append(parts_per_location[neighbour])
            rmv = parts_per_location[neighbour]['locs']
            for loc in rmv:
                del parts_per_location[loc]
    if len(connected_parts) == 2:
        gear_values = [part['value'] for part in connected_parts]
        total += prod(gear_values)
        # print(gear_values, prod(gear_values))
rprint(total)
