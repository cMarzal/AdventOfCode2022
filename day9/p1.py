import operator

data = [(line.split(" ")[0], int(line.split(" ")[1])) for line in open('inp').read().split('\n')]
viewed = set()
h_pos = (0, 0)
t_pos = (0, 0)
viewed.add(t_pos)
rel = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}
for d, num in data:
    for n in range(num):
        h_pos = tuple(map(sum, zip(h_pos, rel[d])))
        if abs(h_pos[0] - t_pos[0]) > 1 or abs(h_pos[1] - t_pos[1]) > 1:
            t_pos = tuple(map(operator.sub, h_pos, rel[d]))
            viewed.add(t_pos)
print(len(viewed))
