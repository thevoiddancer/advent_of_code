from rich import print as rprint

data = "HASH"

data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

def get_hash(string):
    hash_num = 0
    for letter in string:
        hash_num += ord(letter)
        hash_num *= 17
        hash_num %= 256
    return hash_num

print(get_hash(data))
hash_steps = [get_hash(step) for step in data.split(',')]
print(hash_steps)
print(sum(hash_steps))