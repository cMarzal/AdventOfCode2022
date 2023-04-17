dirs = tuple(1 if dir == ">" else -1 for dir in open('inp').read())
shapes = ((0,1,2,3), (1,0+1j,2+1j,1+2j), (0,1,2,2+1j,2+2j), (0,0+1j,0+2j,0+3j), (0,1,0+1j,1+1j))

settled = set()
h_point, dir_n = 0, 0
dir_l = len(dirs)

for x in range(2022):
    shape = set(s+complex(2, h_point+4) for s in shapes[x%5])
    while True:
        this_dir = dirs[dir_n%dir_l]
        dir_n += 1
        if all(coord+this_dir not in settled and coord.real+this_dir in range(7) for coord in shape):
            shape = set(s+this_dir for s in shape)
        if all(coord-1j not in settled and coord.imag > 1 for coord in shape):
            shape = set(s-1j for s in shape)
        else:
            for s in shape:
                settled.add(s)
            h_point = max(s.imag for s in settled)
            break

print(h_point)

