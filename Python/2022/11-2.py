example = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

with open('11.txt', 'r') as file:
    data = file.read()

data = [monkey.split('\n') for monkey in data.split('\n\n')]


class Monkey():
    def __init__(self, data):
        self.items = list(map(int, data[1].split(': ')[1].split(', ')))
        self.rules = lambda old: eval(data[2].split('= ')[1])
        self.test = int(data[3].split('by ')[1])
        self.throw = {
            True: int(data[4].split('monkey ')[1]),
            False: int(data[5].split('monkey ')[1])
        }
        self.inspected = 0

    def inspect(self):
        item = self.items.pop(0)
        item = self.rules(item) % p
        test = item % self.test == 0
        throw_to = self.throw[test]
        self.inspected += 1
        return throw_to, item

    def catch(self, item):
        self.items.append(item)

    def __repr__(self):
        return str(self.items)


monkeys = [Monkey(d) for d in data]
from math import prod as mprod
p = mprod([monkey.test for monkey in monkeys])

for i in range(10000):
    for monkey in monkeys:
        while monkey.items:
            to, item = monkey.inspect()
            monkeys[to].catch(item)
inspected = sorted([monkey.inspected for monkey in monkeys], reverse=True)
print(inspected)
print(inspected[0] * inspected[1])
