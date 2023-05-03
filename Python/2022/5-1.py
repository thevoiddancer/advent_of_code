example = r"""    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

# Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates

with open('5.txt', 'r') as file:
    example = file.read()

crates, instructions = example.split('\n\n')

num_stacks = int(crates[-1])
stacks = ['' for i in range(num_stacks)]
for line in crates.splitlines()[:-1]:
    for i in range(num_stacks):
        if (loc := 1 + 4 * i) < len(line):
            stacks[i] = line[loc].strip() + stacks[i]
stacks = [list(stack) for stack in stacks]

print(stacks)
for instruction in instructions.splitlines():
    print(instruction)
    _, num_to_move, _, from_stack, _, to_stack = instruction.split()
    for _ in range(int(num_to_move)):
        stacks[int(to_stack) - 1].append(stacks[int(from_stack) - 1].pop())
print(stacks)

end = ''
for stack in stacks:
    end += stack.pop()
print(end)