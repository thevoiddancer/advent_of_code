data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

from rich import print as rprint

data = data.split('\n\n')
seeds = [int(x) for x in data.pop(0).split(':')[1].split()]

# print(seeds)

# Split maps to lists with integers
maps = {
    key: [[int(x) for x in val.split()] for val in value.strip().split('\n')] 
    for item in data for key, value in [item.split(':')]
}
# rprint(maps)
# print('maps split to lists')
# rprint(maps)

# Change maps to dicts with integers
for map_name, mappings in maps.items():
    mapping_ranges = []
    for mapping in mappings:
        mapping = [int(x) for x in mapping]
        range_dest = range(mapping[0], mapping[0] + mapping[2])
        range_source = range(mapping[1], mapping[1] + mapping[2])
        delta = mapping[0] - mapping[1]
        d = {'range': range_source, 'delta': delta}
        mapping_ranges.append(d)    
    maps[map_name] = mapping_ranges
# rprint(maps)
# print('maps split to dicts')

# Map through the seeds
locations = []
seed = seeds[0]
for seed in seeds:
    for map_name, mapping in maps.items():
        for mapping_set in mapping:
            if seed in mapping_set['range']:
                seed += mapping_set['delta']
                break
    locations.append(seed)

# print(locations)
print(min(locations))