import sys
sys.setrecursionlimit(9000)

rocks = {tuple(map(int, line.split(","))) for line in open('inp').read().split('\n')}
surfaced, exteriors = 0, set()
limits = tuple((min([rock[x] for rock in rocks]), max([rock[x] for rock in rocks])) for x in range(3))

touching_areas = lambda x,y,z: {(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)}

def find_exterior(pos):
    global exteriors
    exteriors.add(pos)
    to_check = touching_areas(*pos)
    for area in to_check:
        if area not in rocks and area not in exteriors and all(-1 <= a <= 22 for a in area):
            find_exterior(area)

find_exterior((0,0,0))

for rock in rocks:
    check_surfaces = touching_areas(*rock)
    surfaced += sum([1 if rock in exteriors else 0 for rock in check_surfaces])

print(surfaced)
#2558
