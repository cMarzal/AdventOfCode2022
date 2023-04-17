from sympy import symbols, Eq, solve

nums = {line.split(": ")[0]: int(line.split(": ")[1]) if line.split(": ")[1].isnumeric() else
        'nums["' + line.split(" ")[1] + '"] ' + line.split(" ")[2] + ' nums["' + line.split(" ")[3] + '"]' for line in open('inp').read().split('\n')}

nums["root"] = f'{nums["root"].split(" ")[0]} = {nums["root"].split(" ")[2]}'
nums["humn"] = "x"
b = 1
while b:
    for k, v in nums.items():
        if isinstance(v, str):
            if v.count('nums["humn"]') != v.count('nums['):
                for nn in v.split("nums["):
                    if "humn" not in nn and '"' in nn:
                        this_rep = "nums[" + nn.split("]")[0]+"]"
                        #print(this_rep)
                        this_num = f"({eval(this_rep)})"
                        if this_num.count('nums["humn"]') == this_num.count('nums['):
                            nums[k] = v.replace(this_rep, this_num)
                if "humn" not in nums[k]:
                    try:
                        nums[k] = eval(nums[k].replace("nums[", "int(nums[").replace("]", "])"))
                    except: pass
            elif k == "root":
                b = 0

x = symbols('x')
equation = Eq(eval(nums["root"].replace('nums["humn"]', "x").replace("=", "-")), 0)

print(solve(equation, x))

