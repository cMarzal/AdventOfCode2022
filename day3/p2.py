data = [line for line in open('inp').read().split('\n')]
grouped_data = [(data[i], data[i+1], data[i+2]) for i in range(0,len(data), 3)]
common = ["".join(set(p1)&set(p2)&set(p3)) for p1, p2, p3 in grouped_data]
total_priority = sum([(ord(x) -96) % 58 for x in common])
print(total_priority)
