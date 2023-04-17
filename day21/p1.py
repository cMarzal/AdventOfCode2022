nums = {line.split(": ")[0]: int(line.split(": ")[1]) if line.split(": ")[1].isnumeric() else
        'int(nums["' + line.split(" ")[1] + '"]) ' + line.split(" ")[2] + ' int(nums["' + line.split(" ")[3] + '"])' for line in open('inp').read().split('\n')}
b = 1
while b:
    for k, v in nums.items():
        if isinstance(v, str):
            try:
                nums[k] = eval(v)
                b = not k == "root"
            except: pass

print(nums["root"])
