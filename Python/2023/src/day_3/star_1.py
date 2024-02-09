data = """467..617..
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
    location = divmod(conn.start(), width+1)
    connection_locations[location] = conn.group()

# Remove parts that are connected
for location in connection_locations:
    for step in neighbours:
        neighbour = tuple(map(add, location, step))
        if neighbour in parts_per_location:
            rmv = parts_per_location[neighbour]['locs']
            for loc in rmv:
                del parts_per_location[loc]
# rprint(parts_per_location)

resto = []
for loc_rest, values in parts_per_location.copy().items():
    if loc_rest in parts_per_location:
        resto.append(values['value'])
        for rmv in values['locs']:
            del parts_per_location[rmv]

print(resto)

total = []
for loc_rest, values in parts_per_location_backup.copy().items():
    if loc_rest in parts_per_location_backup:
        total.append(values['value'])
        for rmv in values['locs']:
            del parts_per_location_backup[rmv]
print(total)

print(sum(total) - sum(resto))