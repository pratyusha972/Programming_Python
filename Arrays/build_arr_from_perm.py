#Problem:https://leetcode.com/problems/build-array-from-permutation/
nums = [0,2,1,5,3,4]
new_nums = []
for i in range(len(nums)):
    new_nums.append(nums[nums[i]])
print(new_nums)
