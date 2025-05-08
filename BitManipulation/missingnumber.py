#Problem:https://leetcode.com/problems/missing-number/
nums = [9,6,4,2,3,5,7,0,1]
# xor = len(nums)
# for i in range(len(nums)):
#     xor ^= nums[i]
#     xor ^= i
# print(xor)
l = len(nums)
sums = l
sumi = 0
for i in range(l):
    sums += i
    sumi += nums[i]
print(sums - sumi)
