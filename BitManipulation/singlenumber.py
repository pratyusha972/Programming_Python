#Problem:https://leetcode.com/problems/single-number/
nums = [4,1,2,1,2]
# freq = Counter(nums)
# ans = None
# for key, val in freq.items():
#     if val == 1:
#         ans = key
xor=0
for i in range(len(nums)):
    xor ^= nums[i]
print(xor)
