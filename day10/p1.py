data = [(1, 0) if line == "noop" else (2, int(line.split(" ")[1])) for line in open('inp').read().split('\n')]
cycle = 1
value = 1
total_strength = 0
for r, n in data:
    if cycle > 221:
        break
    elif (cycle + 20) % 40 == 0 or (cycle + 19 + r) % 40 == 0:
        total_strength += value * (round(cycle/10)*10)
    cycle += r
    value += n
print(total_strength)
