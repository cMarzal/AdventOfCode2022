data = [(1, 0) if line == "noop" else (2, int(line.split(" ")[1])) for line in open('inp').read().split('\n')]
cycle = 0
value = 1
total_strength = 0
pixels = []
for r, n in data:
    if cycle > 241:
        break
    pixels.extend(["#" if abs((cycle + x) % 40 - value) < 2 else "." for x in range(r)])
    cycle += r
    value += n
for m in range(6):
    print(" ".join(pixels[m*40:(1+m)*40]))
