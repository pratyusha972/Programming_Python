#Problem: https://leetcode.com/problems/search-insert-position/
nums = [1,3]
target = 2
l = len(nums) - 1
left = 0
right = l
ans = None
while left < right:
    mid = left + (right - left)//2
    if mid == 0 and target < nums[mid]:
        ans = 0
        break
    elif nums[mid] >= target and nums[mid-1] < target:
        ans = mid
        break
    elif target > nums[mid]:
        left = mid + 1
    else:
        right = mid
if left == l and nums[left] < target:
    ans = l + 1
elif left == l and nums[left] >= target:
    ans = l
elif left == 0 and nums[left] >= target:
    ans = 0
print(ans) 
