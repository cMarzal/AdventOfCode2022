data = [line for line in open('inp').read().split('\n')]
x_len = len(data)
y_len = len(data[0])
highest_score = 0
for x, row in enumerate(data):
    if x != 0 and x != x_len -1:
        for y in range(y_len):
            if y != 0 and y != y_len - 1:
                s1 = min([y - y2 if row[y] <= row[y2] else y for y2 in range(y)])
                s2 = min([y2+1 if row[y] <= row[y+y2+1] else y_len - y - 1 for y2 in range(y_len-y-1)])
                s3 = min([x-x2 if row[y] <= data[x2][y] else x for x2 in range(x)])
                s4 = min([x2+1 if row[y] <= data[x+x2+1][y] else x_len-x-1 for x2 in range(x_len-x-1)])
                highest_score = max(highest_score, s1*s2*s3*s4)
print(highest_score)
