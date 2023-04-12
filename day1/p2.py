with open('inp', 'r') as inp:
    foods = []
    this_food = 0

    for line in inp:
        line = line.splitlines()[0]
        if line == "":
            foods.append(this_food)
            this_food = 0
        else:
            this_food += int(line)
print(sum(sorted(foods)[-3:]))
