current_folder = []
sizes = {}
this_dir = {}
ls = 0


def this_level(folder, dict):
    this_dict = dict
    for f in folder:
        this_dict = this_dict[f]
    return this_dict


for line in open('inp').read().split('\n'):
    if line.startswith("$"):
        if ls == 1:
            this_dict = sizes
            for f in current_folder[:-1]:
                this_dict = this_dict[f]
            this_dict[current_folder[-1]] = this_dir.copy()
            ls = 0
            this_dir = {}
        if line.startswith("$ cd /"):
            current_folder = ["/"]
        elif line.startswith("$ cd .."):
            current_folder = current_folder[:-1]
        elif line.startswith("$ cd "):
            current_folder.append(line.split(" ")[2])
    else:
        ls = 1
        if line.startswith("dir"):
            this_dir[line.split(" ")[1]] = {}
        else:
            this_dir[line.split(" ")[1]] = int(line.split(" ")[0])

this_dict = sizes
for f in current_folder[:-1]:
    this_dict = this_dict[f]
this_dict[current_folder[-1]] = this_dir.copy()

final_sizes = 0


def checksums(d):
    global final_sizes
    this_size = 0
    for k, v in d.items():
        if type(v) == dict:
            this_size += checksums(v)
        else:
            this_size += v
    if this_size <= 100000:
        final_sizes += this_size
    return this_size


total_sizes = checksums(sizes)

print(final_sizes)
