data = [(line[:int(len(line)/2)], line[int(len(line)/2):]) for line in open('inp').read().split('\n')]
common = ["".join(set(p1)&set(p2)) for p1, p2 in data]
total_priority = sum([(ord(x) -96) % 58 for x in common])
print(total_priority)
