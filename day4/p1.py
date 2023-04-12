data = [(line.split(",")[0].split("-"), line.split(",")[1].split("-")) for line in open('inp').read().split('\n')]
total_contained = sum([1 if (int(l1) <= int(l2) and int(h1) >= int(h2)) or (int(l2) <= int(l1) and int(h2) >= int(h1)) else 0 for (l1, h1), (l2, h2) in data])
print(total_contained)