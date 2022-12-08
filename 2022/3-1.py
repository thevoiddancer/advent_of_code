# The list of items for each rucksack is given as characters all on a single line.
# A given rucksack always has the same number of items in each of its two compartments,
# so the first half of the characters represent items in the first compartment,
# while the second half of the characters represent items in the second compartment.

example = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

# The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means
#   its first compartment contains the items vJrwpWtwJgWr, while the second compartment
#   contains the items hcsFMMfFFhFp. The only item type that appears in both
#   compartments is lowercase p.
# The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL.
#   The only item type that appears in both compartments is uppercase L.
# The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common
#   item type is uppercase P.
# The fourth rucksack's compartments only share item type v.
# The fifth rucksack's compartments only share item type t.
# The sixth rucksack's compartments only share item type s.


def common(text):
    return list(set(text[:len(text)//2]) & set(text[len(text)//2:]))[0]


def score(letter):
    return ord(letter.lower()) - ord('a') + 1 + (26 if letter.isupper() else 0)


with open('3.py', 'r') as file:
    print(sum([score(common(line)) for line in file.read().strip('\n').splitlines()]))

# a = 'vJrwpWtwJgWrhcsFMMfFFhFp'
# score(common(a))
