data = tuple((int(line.split("=")[1].split(",")[0]),
               int(line.split("=")[2].split(":")[0]),
               int(line.split("=")[3].split(",")[0]),
               int(line.split("=")[4])) for line in open('inp').read().split('\n'))

not_in, d_lines, u_lines = set(), set(), set()
max_coord = 10

for x1, y1, x2, y2 in data:
    dist = abs(x1-x2) + abs(y1-y2)
    d_lines.add(y1 - x1 + dist)
    d_lines.add(y1 - x1 - dist)
    u_lines.add(y1 + x1 - dist)
    u_lines.add(y1 + x1 + dist)

cons_d, cons_u = 0, 0

for d1, d2 in zip(sorted(d_lines), sorted(d_lines)[1:]):
    if d2 - d1 == 2:
        cons_d = d2-1
for u1, u2 in zip(sorted(u_lines), sorted(u_lines)[1:]):
    if u2 - u1 == 2:
        cons_u = u2-1

point = (int((cons_u - cons_d)/2), cons_u - int((cons_u - cons_d)/2))

print(point[0] * 4000000 + point[1])
