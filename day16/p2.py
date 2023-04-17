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
dists = {k1: {k2: v2 for k2, v2 in dists_tmp[k1].items() if k2 in opened} for k1 in opened}
dists["AA"] = {k2: v2 for k2, v2 in dists_tmp["AA"].items() if k2 in opened}
max_turn = 26
cache = {}
del data_tmp, dists_tmp


def check_valve(turn, valve, op, released):
    global cache
    try:
        sol, op2 = cache[(turn, valve, op.values())]
        return released + sol, op2.copy()
    except:
        if valve != "AA":
            released += (max_turn - turn) * flows[valve]
            op[valve] = 1
            turn += 1
            if turn >= max_turn - 1:
                return released, op
        this_rel = released
        this_op = op.copy()
        for vv in dists[valve]:
            if op[vv] == 0 and dists[valve][vv] + turn < max_turn:
                new_rel, op3 = check_valve(turn + dists[valve][vv], vv, op.copy(), released)
                if new_rel > this_rel:
                    this_rel = new_rel
                    this_op = op3.copy()
    cache[(turn, valve, op.values())] = (this_rel - released, op.copy())
    return this_rel, this_op.copy()


me_rel, me_op = check_valve(1, "AA", opened.copy(), 0)
print(me_op)
print(check_valve(1, "AA", me_op.copy(), me_rel))
