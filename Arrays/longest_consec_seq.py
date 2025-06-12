#Problem:https://leetcode.com/problems/longest-consecutive-sequence/
nums = [100,4,200,1,3,2]
set_nums = set(nums)
maxcount = 0
for num in set_nums:
    if num - 1 in set_nums:
        continue
    count = 1
    while num + 1 in set_nums:
        count += 1
        num += 1
    maxcount = max(count, maxcount)
print(maxcount)
