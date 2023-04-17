data_tmp = {line.split(" ")[1]: (int(line.split("=")[1].split(";")[0]), tuple(line.split(" ", 9)[9].split(", "))) for
            line in open('inp').read().split('\n')}

dists_tmp = {k1: {k2: 1 if k2 in data_tmp[k1][1] else len(data_tmp) for k2 in data_tmp} for k1 in
             data_tmp}
for k in dists_tmp:
    for i in dists_tmp:
        for j in dists_tmp:
            dists_tmp[i][j] = min(dists_tmp[i][j], dists_tmp[i][k] + dists_tmp[k][j])

opened = {k: 0 for k, (f, v) in data_tmp.items() if f != 0}
flows = {k: f for k, (f, v) in data_tmp.items() if f != 0}
dists = {k1: {k2: v2 for k2, v2 in dists_tmp[k1].items() if k2 in opened} for k1 in set(opened.keys()) | {"AA"}}
max_turn = 30
cache = {}
del data_tmp, dists_tmp


def check_valve(turn, valve, op, released):
    global cache
    try:
        sol = cache[(turn, valve, op.values())]
        return released + sol
    except:
        if valve != "AA":
            released += (max_turn - turn) * flows[valve]
            op[valve] = 1
            turn += 1
            if turn >= max_turn - 1:
                return released
        this_rel = {released}
        for vv in dists[valve]:
            if op[vv] == 0 and dists[valve][vv] + turn < 30:
                this_rel.add(check_valve(turn + dists[valve][vv], vv, op.copy(), released))
    cache[(turn, valve, op.values())] = max(this_rel) - released
    return max(this_rel)


print(check_valve(1, "AA", opened.copy(), 0))
