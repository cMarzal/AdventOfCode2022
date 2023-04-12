data = [(line.split(",")[0].split("-"), line.split(",")[1].split("-")) for line in open('inp').read().split('\n')]
total_overlap = sum([1 if (int(l1) <= int(l2) <= int(h1)) or (int(l2) <= int(l1) <= int(h2)) else 0 for (l1, h1), (l2, h2) in data])
print(total_overlap)