with open('inp', 'r') as inp:
    max_food = 0
    this_food = 0

    for line in inp:
        line = line.splitlines()[0]
        if line == "":
            max_food = max(this_food, max_food)
            this_food = 0
        else:
            this_food += int(line)
print(max_food)
