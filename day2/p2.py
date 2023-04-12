data = [line.split(" ") for line in open('inp').read().split('\n')]

total_points = sum([(ord(us) - 88)*3 + ((1 + (ord(us) - 88) + (ord(op) - 64)) % 3) + 1 for op, us in data])
print(total_points)
