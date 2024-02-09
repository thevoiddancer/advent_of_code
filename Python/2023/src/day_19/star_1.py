data = r"""px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

rules, items = data.split("\n\n")
rules = rules.splitlines()

rules = {name: ruleset[:-1] for name, ruleset in [rule.split("{") for rule in rules]}
rules = {
    name: {
        cond: dest
        for cond, dest in [
            rule.split(":") for rule in process.split(",") if len(rule.split(":")) == 2
        ]
        + [[True, process.split(",")[-1]]]
    }
    for name, process in rules.items()
}

items = [item[1:-1].split(",") for item in items.splitlines()]
items = [dict([pair.split("=") for pair in item]) for item in items]
items = [{k: int(v) for k, v in item.items()} for item in items]
rules

accepted = []
for item in items:
    # print(item)
    workflow = "in"
    # print(workflow)
    while workflow not in "AR":
        # print(rules[workflow])
        for cond, dest in rules[workflow].items():
            if type(cond) != bool:
                # print(cond, dest, eval(item[cond[0]] + cond[1:]))
                if eval(str(item[cond[0]]) + cond[1:]):
                    workflow = dest
                    break
            else:
                # print(cond, dest, cond)
                workflow = dest
            # print(workflow)
    if workflow == "A":
        accepted.append(sum(item.values()))

print(sum(accepted))