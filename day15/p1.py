data = tuple((int(line.split("=")[1].split(",")[0]),
              int(line.split("=")[2].split(":")[0]),
              int(line.split("=")[3].split(",")[0]),
              int(line.split("=")[4])) for line in open('inp').read().split('\n'))

not_in_y = set()
find_y = 2000000
s_b_in_y = set(row[2] for row in data if row[3] == find_y)

for x1, y1, x2, y2 in data:
    dist = abs(x1 - x2) + abs(y1 - y2)
    if y1 - dist <= find_y <= y1 + dist:
        not_in_y.add(x1)
        dist_rm = min(y1 + dist - find_y, find_y + dist - y1)
        for i in range(dist_rm):
            not_in_y.add(x1 + i + 1)
            not_in_y.add(x1 - i - 1)

print(len(not_in_y - s_b_in_y))
