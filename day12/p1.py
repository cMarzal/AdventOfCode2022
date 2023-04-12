import sys
sys.setrecursionlimit(5000)

data_temp = tuple(
    [tuple([27 if l == "E" else max(0, ord(l) - 96) for l in line]) for line in open('inp').read().split('\n')])
start = (0, 0)
end = (0, 0)
for i, subtuple in enumerate(data_temp):
    if 27 in subtuple:
        end = (i, subtuple.index(27))
    if 0 in subtuple:
        start = (i, subtuple.index(0))
size_y = len(data_temp)
size_x = len(data_temp[0])
data_temp = ()
data = tuple(
    [tuple([26 if l == "E" else max(1, ord(l) - 96) for l in line]) for line in open('inp').read().split('\n')])

dists = [[9999 for x in range(size_x)] for y in range(size_y)]


def get_lengths(pos, steps):
    dists[pos[0]][pos[1]] = steps
    if pos != start:
        for i in range(-1, 2, 2):
            index_x = pos[1] + i
            if -1 < index_x < size_x:
                if data[pos[0]][index_x] >= data[pos[0]][pos[1]] - 1 and steps + 1 < dists[pos[0]][index_x]:
                    get_lengths((pos[0], index_x), steps + 1)
            index_y = pos[0] + i
            if -1 < index_y < size_y:
                if data[index_y][pos[1]] >= data[pos[0]][pos[1]] - 1 and steps + 1 < dists[index_y][pos[1]]:
                    get_lengths((index_y, pos[1]), steps + 1)


get_lengths(end, 0)
print(dists[start[0]][start[1]])
