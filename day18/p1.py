rocks = tuple(tuple(map(int, line.split(","))) for line in open('inp').read().split('\n'))
surfaced = 0
for rock in rocks:
    check_surfaces = tuple(tuple(rock_ax + y if r == x else rock_ax for r, rock_ax in enumerate(rock)) for y in range(-1, 2, 2) for x in range(3))
    surfaced += sum([0 if rock in rocks else 1 for rock in check_surfaces])

print(surfaced)
