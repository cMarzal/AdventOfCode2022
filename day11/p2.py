import math
from functools import reduce

data = [[[int(x) for x in monkey.split("\n")[1].split("items: ")[1].split(", ")], # 0- items
         monkey.split("\n")[2].split("new = ")[1], # 1- operation
         int(monkey.split("\n")[3].split("by ")[1]), # 2- divisible by
         int(monkey.split("\n")[4].split("monkey ")[1]), # 3- if true
         int(monkey.split("\n")[5].split("monkey ")[1]), # 4- if false
         0 # 5- times inspected
         ] for monkey in open('inp').read().split('\n\n')]

divs = [m[2] for m in data]
lcm = reduce(lambda x,y:math.lcm(x,y),divs)

for r in range(10000):
    for monkey in data:
        for old in monkey[0]:
            monkey[5] += 1
            old = eval(monkey[1])%lcm
            if old % monkey[2] == 0:
                data[monkey[3]][0].append(old)
            else:
                data[monkey[4]][0].append(old)
        monkey[0] = []

inspected = [m[5] for m in data]
inspected.sort(reverse=True)
print(inspected[0]*inspected[1])
