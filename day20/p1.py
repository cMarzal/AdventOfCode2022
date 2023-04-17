nums = tuple(int(line) for line in open('inp').read().split('\n'))
nums_len = len(nums)
indexes = list(range(nums_len))
for ind, num in enumerate(nums):
    this_ind = indexes[ind]
    new_ind = (this_ind+num)%(nums_len-1)
    if new_ind > this_ind:
        indexes = [i - 1 if this_ind < i <= new_ind else i for i in indexes]
    elif new_ind < this_ind:
        indexes = [i + 1 if new_ind <= i < this_ind else i for i in indexes]
    indexes[ind] = new_ind

ind_0 = indexes[nums.index(0)]
print(nums[indexes.index((ind_0+1000)%nums_len)] + nums[indexes.index((ind_0+2000)%nums_len)] + nums[indexes.index((ind_0+3000)%nums_len)])
