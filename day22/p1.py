x = open("inp", "r").read()
grid, ins = x.split("\n\n")

grid = grid.split("\n")
width = max([len(line) for line in grid])
height = len(grid)
grid = [" " + line.ljust(width) + " " for line in grid]
width += 2
height += 2
grid = [" "*width] + grid + [" "*width]

ins_list = []
buffer = ""
for c in ins.strip("\n"):
    if c in "LR":
        if buffer != "":
            ins_list += [int(buffer)]
            buffer = ""
        ins_list += [c]
    else:
        buffer += c

if buffer != "":
    ins_list += [int(buffer)]
    buffer = ""

x=y=1
dir = 0
dir_lookup = [[0,1],[1,0],[0,-1],[-1,0]]
for j in range(width):
    if grid[1][j] == ".":
        y=j
        break
dir_cache = (x,y)

for step in ins_list:
    if step == "R":
        dir = (dir+1)%4
    elif step == "L":
        dir = (dir-1)%4
    else:
        dx,dy = dir_lookup[dir]
        for i in range(step):
            nx,ny = x+dx,y+dy
            if grid[nx][ny] == " ":
                while True:
                    nx,ny = nx-dx,ny-dy
                    if grid[nx][ny] == " ":
                        break
                nx,ny = nx+dx,ny+dy
            if grid[nx][ny] == "#":
                break
            x,y = nx,ny

print(x*1000+y*4+dir)
