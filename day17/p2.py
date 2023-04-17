dirs = tuple(1 if dir == ">" else -1 for dir in open('inp').read())
shapes = ((0,1,2,3), (1,0+1j,2+1j,1+2j), (0,1,2,2+1j,2+2j), (0,0+1j,0+2j,0+3j), (0,1,0+1j,1+1j))

settled, cache = set(), dict()
h_point, dir_n = 0, 0
dir_l = len(dirs)
turns = 1000000000000

for x in range(turns):
    shape = set(s+complex(2, h_point+4) for s in shapes[x%5])
    while True:
        dir_ord = dir_n%dir_l
        this_dir = dirs[dir_ord]
        dir_n += 1
        if all(coord+this_dir not in settled and coord.real+this_dir in range(7) for coord in shape):
            shape = set(s+this_dir for s in shape)
        if all(coord-1j not in settled and coord.imag > 1 for coord in shape):
            shape = set(s-1j for s in shape)
        else:
            for s in shape:
                settled.add(s)
            h_point = max(h_point, max(s.imag for s in shape))
            max_x = tuple([int(min([h_point - s.imag if s.real == n else 100 for s in settled])) for n in range(7)])
            c_key = (x%5, dir_ord, max_x)
            if c_key in cache:
                prev_x, prev_h = cache[c_key]
                tot_times = int((turns-prev_x)/(x - prev_x))
                tot_rem = (turns-prev_x) - (tot_times * (x - prev_x))
                h_rem = max([h for (x2, h) in cache.values() if x2 == tot_rem + prev_x])
                tot_h = ((h_point - prev_h) * tot_times) + h_rem
                print(tot_h-1)
                exit()
            else:
                cache[c_key] = (x, h_point)
            break

print(h_point)
