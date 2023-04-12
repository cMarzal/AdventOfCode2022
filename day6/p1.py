line = open('inp').read()
for n, letter in enumerate(line):
    last = line[n-4:n]
    if len(set(last)) == 4:
        print(n)
        break
