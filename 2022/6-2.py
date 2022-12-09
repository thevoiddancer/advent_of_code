# The device will send your subroutine a datastream buffer (your puzzle input);
# your subroutine needs to identify the first position where the four most
# recently received characters were all different.

examples = """mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

res = [5, 6, 10, 11]

# for example in examples.splitlines():
#     print(example)

with open('6.txt', 'r') as file:
    example = file.read()

    marker_length = 14
    for i in range(len(example) - marker_length):
        sequence = example[i: i + marker_length]
        if len(set(sequence)) == marker_length:
            print(i + marker_length)
            break
