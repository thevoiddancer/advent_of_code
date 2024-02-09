from rich import print as rprint

data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

data = [[int(value) for value in line.split()] for line in data.splitlines()]

# data = [data[153]]

to_add = []
# print(data)
for window in data:
    # print(window)
    orig = window[-1]
    last_vals = []
    # while sum(window) != 0:
    while any([x != 0 for x in window]):
        window = list(zip(window[:-1], window[1:]))
        for idx, pair in enumerate(window):
            window[idx] = pair[1] - pair[0]
        last_vals.append(window[-1])
        # print(window)
    missing_value = sum(last_vals) + orig
    to_add.append(missing_value)
    # print(missing_value)
# print(to_add)
print(sum(to_add))