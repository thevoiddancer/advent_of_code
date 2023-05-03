from functools import reduce

# The only way to tell which item type is the right one is by finding the one item
#   type that is common between all three Elves in each group.

# Every set of three lines in your list corresponds to a single group, but each
#   group can have a different badge item type. So, in the above example, the first
#   group's rucksacks are the first three lines:

example = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
rZsJsPPZsGzwwsLwLmpwMDw"""

# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg

# And the second group's rucksacks are the next three lines:

# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw

# In the first group, the only item type that appears in all three rucksacks is
#   lowercase r; this must be their badges. In the second group, their badge item type must be Z.

# Priorities for these items must still be found to organize the sticker attachment
#   efforts: here, they are 18 (r) for the first group and 52 (Z) for the second
#   group. The sum of these is 70.


def score(letter):
    return ord(letter.lower()) - ord('a') + 1 + (26 if letter.isupper() else 0)


def split_by_3(text):
    return [text.splitlines()[3*i:3*i+3] for i in range(0, len(text.splitlines())//3)]


def common(triple):
    triple = [set(i) for i in triple]
    return list(reduce(lambda a, b: a & b, triple))[0]


with open('3.py', 'r') as file:
    data_triple = split_by_3(file.read())

sum([score(common(trip)) for trip in data_triple])