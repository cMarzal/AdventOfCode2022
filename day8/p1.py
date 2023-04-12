data = [line for line in open('inp').read().split('\n')]
x_len = len(data)
y_len = len(data[0])
total_view = 0
for x, row in enumerate(data):
    if x == 0 or x == x_len -1:
        total_view += y_len
    else:
        for y in range(y_len):
            if y == 0 or y == y_len - 1:
                total_view += 1
            else:
                if sum([1 if row[y] <= row[y2] else 0 for y2 in range(y)]) == 0:
                    total_view += 1
                elif sum([1 if row[y] <= row[y+y2+1] else 0 for y2 in range(y_len-y-1)]) == 0:
                    total_view += 1
                elif sum([1 if row[y] <= data[x2][y] else 0 for x2 in range(x)]) == 0:
                    total_view += 1
                elif sum([1 if row[y] <= data[x+x2+1][y] else 0 for x2 in range(x_len-x-1)]) == 0:
                    total_view += 1
print(total_view)