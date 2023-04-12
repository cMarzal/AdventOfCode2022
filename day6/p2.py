line = open('inp').read()
for n, letter in enumerate(line):
    last = line[n-14:n]
    if len(set(last)) == 14:
        print(n)
        break
