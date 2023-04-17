from ast import literal_eval

data = tuple([(literal_eval(line.split("\n")[0]), literal_eval(line.split("\n")[1])) for line in
              open('inp').read().split('\n\n')])


def checkList(l1, l2):
    for left, right in zip(l1, l2):
        this_r = 0
        match left, right:
            case int(), int():
                this_r = left - right
            case list(), list():
                this_r = checkList(left, right)
            case list(), int():
                this_r = checkList(left, [right])
            case int(), list():
                this_r = checkList([left], right)
        if this_r != 0:
            return this_r
    return len(l1) - len(l2)


sum_i = 0
for index, (d1, d2) in enumerate(data):
    if checkList(d1, d2) < 1:
        sum_i += index + 1

print(sum_i)
