position = ["" for a in range(9)]
moves = []

for n, line in enumerate(open('inp').read().split('\n')):
    if n < 8:
        for i in range(9):
            cr = line[1 + (i * 4)]
            if cr != " ":
                position[i] = cr + position[i]
    elif n > 9:
        moves.append((int(line.split(" ")[1]), int(line.split(" ")[3])-1, int(line.split(" ")[5])-1))

for move in moves:
    moved_crates = position[move[1]][-move[0]:][::-1]
    position[move[1]] = position[move[1]][:-move[0]]
    position[move[2]] += moved_crates

print(''.join([stack[-1] for stack in position]))
