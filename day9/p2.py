import operator

data = [(line.split(" ")[0], int(line.split(" ")[1])) for line in open('inp').read().split('\n')]
viewed = set()
h_pos = [(0, 0) for x in range(10)]
viewed.add(h_pos[9])
rel = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}
for d, num in data:
    for n in range(num):
        h_pos[0] = tuple(map(sum, zip(h_pos[0], rel[d])))
        moved_pos = rel[d]
        for p in range(9):
            if abs(h_pos[p][0] - h_pos[p+1][0]) > 1 or abs(h_pos[p][1] - h_pos[p+1][1]) > 1:
                last_pos = h_pos.copy()[p+1]
                if abs(moved_pos[0]) > 0 and abs(moved_pos[1]) > 0:
                    if abs(h_pos[p][0] - h_pos[p + 1][0]) == 0:
                        h_pos[p + 1] = (h_pos[p][0], h_pos[p][1] - moved_pos[1])
                    elif abs(h_pos[p][1] - h_pos[p + 1][1]) == 0:
                        h_pos[p + 1] = (h_pos[p][0] - moved_pos[0], h_pos[p][1])
                    else:
                        h_pos[p+1] = tuple(map(sum, zip(h_pos[p+1], moved_pos)))
                else:
                    h_pos[p+1] = tuple(map(operator.sub, h_pos[p], moved_pos))
                moved_pos = tuple(map(operator.sub, h_pos[p+1], last_pos))
            else:
                moved_pos = (0, 0)
        viewed.add(h_pos[9])
print(len(viewed))
