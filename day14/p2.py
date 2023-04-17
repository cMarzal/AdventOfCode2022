data = tuple([tuple([*map(eval, line.split('->'))]) for line in open('inp').read().split('\n')])

walls = set()
for row in data:
    for (x1, y1), (x2, y2) in zip(row, row[1:]):
        walls.update(
            [complex(x, y) for x in range(min(x1, x2), max(x1, x2) + 1) for y in range(min(y1, y2), max(y1, y2) + 1)])

sand = 500
lowest_y = max([wall.imag for wall in walls]) + 1
sand_count = 0

while True:
    for next_sand in sand + 1j, sand - 1 + 1j, sand + 1 + 1j:
        if next_sand not in walls and sand.imag != lowest_y:
            sand = next_sand
            break
    else:
        walls.add(sand)
        sand_count += 1
        sand = 500
    if 500 in walls:
        print(sand_count)
        break
