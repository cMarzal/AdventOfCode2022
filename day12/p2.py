import sys

sys.setrecursionlimit(5000)

data = tuple(
    [tuple([27 if l == "E" else max(1, ord(l) - 96) for l in line]) for line in open('inp').read().split('\n')])
end = (0, 0)
for i, subtuple in enumerate(data):
    if 27 in subtuple:
        end = (i, subtuple.index(27))

size_y = len(data)
size_x = len(data[0])
dists = [[9999 for x in range(size_x)] for y in range(size_y)]


def get_lengths(pos, steps):
    dists[pos[0]][pos[1]] = steps
    if data[pos[0]][pos[1]] != 1:
        for i in range(-1, 2, 2):
            index_x = pos[1] + i
            if -1 < index_x < size_x:
                if (data[pos[0]][index_x] >= data[pos[0]][pos[1]] - 1 or data[pos[0]][index_x] == 25) and steps + 1 < \
                        dists[pos[0]][index_x]:
                    get_lengths((pos[0], index_x), steps + 1)
            index_y = pos[0] + i
            if -1 < index_y < size_y:
                if (data[index_y][pos[1]] >= data[pos[0]][pos[1]] - 1 or data[index_y][pos[1]] == 25) and steps + 1 < \
                        dists[index_y][pos[1]]:
                    get_lengths((index_y, pos[1]), steps + 1)


get_lengths(end, 0)
as_pos = set([(y, x) if data[y][x] == 1 else (0, 0) for x in range(size_x) for y in range(size_y)])
min_dist = 9999
for py, px in as_pos:
    min_dist = min(min_dist, dists[py][px])
print(min_dist)
