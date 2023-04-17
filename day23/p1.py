from collections import Counter

with open("inp") as r:
    s = r.read().rstrip()
    lines = s.split('\n')
    lgroups = s.split('\n\n')

elfs = {x + 1j * y for y, row in enumerate(lines) for x, c in enumerate(row) if c == '#'}
x8 = [1, 1 + 1j, 1j, 1j - 1, -1, -1 - 1j, -1j, 1 - 1j]
dirs = [-1j, 1j, -1, 1]


def move(elves, p, fdir):
    adj = elves & {p + t for t in x8}
    if not adj: return p
    for t in range(4):
        d = dirs[(fdir + t) % 4]
        adj = elves & {p + d, p + d + d * 1j, p + d - d * 1j}
        if not adj: return p + d
    return p


def empty_ground(elves):
    xs = [elf.real for elf in elves]
    ys = [elf.imag for elf in elves]
    return (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1) - len(elves)


def update(elves, r):
    want = {elf: move(elves, elf, r % 4) for elf in elves}
    c = Counter(want.values())
    canhave = {elf for elf in want if c[want[elf]] == 1}
    canthave = elves - canhave
    return canthave | {want[elf] for elf in canhave}


pelfs = {}
for i in range(10):
    pelfs = elfs
    elfs = update(elfs, i)

print(int(empty_ground(elfs)))
