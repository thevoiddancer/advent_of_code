from rich import print as rprint

data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

data = [[int(value) for value in line.split()] for line in data.splitlines()]

# data = [data[153]]

to_add = []
for window in data:
    # print(window)
    first_vals = []
    first_vals.append(window[0])
    while any([x != 0 for x in window]):
        window = [b - a for a, b in zip(window[:-1], window[1:])]
        first_vals.append(window[0])
        # print(window)
    # print(first_vals)
    first_vals_rev = first_vals[::-1]
    missing = [0]
    for val in first_vals_rev[1:]:
        missing.append(val-missing[-1])
    # print(missing)
    # print(missing[-1])
    to_add.append(missing[-1])
print(to_add)
print(sum(to_add))