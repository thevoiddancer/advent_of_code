data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

max_colors = {'red': 12, 'green': 13, 'blue': 14}

from math import prod

result = 0
for game in data.splitlines():
    max_count = {color: 0 for color in max_colors}
    id, sets = game.split(':')
    id = id.split()[1]
    for reveal in sets.split(';'):
        for cubes in reveal.split(','):
            count, color = cubes.split()
            if max_count[color] < int(count):
                max_count[color] = int(count)
    possible = True
    power = prod(max_count.values(), start=1)
    # print(max_count, power)
    for color in max_colors:
        if max_count[color] > max_colors[color]:
            possible = False
    # if possible:
    result += power

print(result)
