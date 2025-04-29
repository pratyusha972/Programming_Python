#Problem:https://leetcode.com/problems/jump-game/description/
#can solve using recursive, DP - memoization and tabulation methods also. However, time complexity for recursion is O(N^N), and memoization and tabulation take O(N*N), while greedy solution just takes O(N).
#Greedy
r = 0
for i in range(len(nums)-1):
    if nums[i] > 0 and r >= i:
        r = max(r, i + nums[i])
if r >= len(nums) - 1:
    print(True)
print(False)
