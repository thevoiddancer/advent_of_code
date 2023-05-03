# The device will send your subroutine a datastream buffer (your puzzle input);
# your subroutine needs to identify the first position where the four most
# recently received characters were all different.

examples = """bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

res = [5, 6, 10, 11]

# for example in examples.splitlines():
#     print(example)

with open('6.txt', 'r') as file:
    example = file.read()
    for i in range(len(example) - 4):
        sequence = example[i: i+4]
        if len(set(sequence)) == 4:
            print(i+4)
            break
