data = """Time:        40     81     77     72
Distance:   219   1012   1365   1089"""

from math import sqrt, floor, ceil, prod
def roots(a, b, c):
    p = -b
    q = sqrt(b**2 - 4*a*c)
    x2 = (p+q)/(2*a)
    x1 = (p-q)/(2*a)
    return x1, x2

def record_beating(T, D):
    x1, x2 = roots(1, -T, D)
    x1 = ceil(x1 if x1 % 1 else x1 + 1)
    x2 = floor(x2 if x2 % 1 else x2 - 1)
    return x2 - x1 + 1

time, distance = [int(''.join(line.split(':')[1].split())) for line in data.splitlines()]
# print(time, distance)

print(record_beating(time, distance))

# print(prod(beating_options))