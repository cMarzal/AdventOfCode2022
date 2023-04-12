data = [line.split(" ") for line in open('inp').read().split('\n')]
total_points = sum([(ord(us) - 87) + 3 * ((4 + (ord(us) - 87) - (ord(op) - 64)) % 3) for op, us in data])
print(total_points)
