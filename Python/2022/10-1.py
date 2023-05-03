example = """noop
addx 3
addx -5"""

with open('10.txt', 'r') as file:
    data = file.read()

data = data.splitlines()
dur = {'noop': 1, 'addx': 2}


def apply_ins(inst, count, reg):
    cmd, *val = inst.split()
    count += dur[cmd]
    if cmd == 'addx':
        reg += int(val[0])
    return count, reg


read = [20, 60, 100, 140, 180, 220]
signal = {}
reg = 1
count = 1
for inst in data:
    if not read:
        continue
    if count + (1 if inst == 'noop' else 2) > read[0]:
        signal[read[0]] = reg
        read.pop(0)
    count, reg = apply_ins(inst, count, reg)


s = 0
print(signal)
for time, value in signal.items():
    s += time * value
print(s)
