# However, as some of the Elves compare their section assignments with each other,
# they've noticed that many of the assignments overlap. To try to quickly find
# overlaps and reduce duplicated effort, the Elves pair up and make a big list
# of the section assignments for each pair (your puzzle input).
#
# For example, consider the following list of section assignment pairs:
#
example = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
#
# For the first few pairs, this list means:
#
#     Within the first pair of Elves, the first Elf was assigned sections 2-4
#           (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
#     The Elves in the second pair were each assigned two sections.
#     The Elves in the third pair were each assigned three sections: one got
#           sections 5, 6, and 7, while the other also got 7, plus 8 and 9.
#
# Some of the pairs have noticed that one of their assignments fully contains the other.
# For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where
# one assignment fully contains the other, one Elf in the pair would be exclusively
# cleaning sections their partner will already be cleaning, so these seem like the
# most in need of reconsideration. In this example, there are 2 such pairs.
#
# In how many assignment pairs does one range fully contain the other?

with open('4.txt', 'r') as file:
    example = file.read()

example = [[[int(section) for section in assignment.split('-')] for assignment in line.split(',')] for line in example.splitlines()]

from rich import print as rprint

overlap = 0
for pair in example:
    if (
        max(pair[0]) >= min(pair[1]) and min(pair[0]) <= max(pair[1])
    ):
        print(pair)
        overlap += 1

print(overlap)
