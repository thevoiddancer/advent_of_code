import re
data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

output_list = []
for line in data.splitlines():
    patt = re.compile(r'[a-zA-Z]*(\d)')
    match = re.findall(patt, line)
    output_list.append(int(f'{match[0]}{match[-1]}'))
print(sum(output_list))
