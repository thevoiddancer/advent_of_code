example = """noop
addx 3
addx -5"""

with open('10.txt', 'r') as file:
    data = file.read()

data = data.splitlines()
dur = {'noop': 1, 'addx': 2}
reg = 1
count = 0
values = [reg]


def apply_ins(inst, count, reg):
    cmd, *val = inst.split()
    val = int(val[0]) if val else 0
    values.append(reg)
    count += dur[cmd]
    reg += val
    if cmd == 'addx':
        values.append(reg)
    return count, reg


for inst in data:
    count, reg = apply_ins(inst, count, reg)
lcd_data = [[x for x in values[0 + 40 * rownum:40 + 40 * rownum]] for rownum in range(6)]
print('\n'.join([''.join(["#" if abs(loc-val) < 2 else " " for loc, val in enumerate(row)]) for row in lcd_data]))
