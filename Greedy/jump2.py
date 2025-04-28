nums = [2,3,1,1,4]
#recursion
#def recur(pos, nums, jumps):
#     if pos == len(nums)-1:
#         return jumps
#     minjump = float('inf')
#     for i in range(1, nums[pos]+1):
#         if pos + i < len(nums):
#             minjump = min(minjump, recur(pos+i, nums, jumps+1))
#     return minjump
# print(recur(0, nums, 0))

# #memoization
# def recur(pos, nums, dp):
#     l = len(nums)
#     if pos == l-1:
#         dp[l-1] = 0
#         return dp
#     minjump = float('inf')
#     for i in range(1, nums[pos]+1):
#         jump = pos + i
#         if jump < l:
#             if jump not in dp.keys():
#                 dp = recur(jump, nums, dp)
#             minjump = min(minjump, dp[jump])
#     dp[pos] = minjump + 1
#     return dp
# d = recur(0, nums, {})
# print(d[0])

# #Tabulation1
# l = len(nums)
# dp = [float('inf') for i in range(l)]
# dp[l-1] = 0
# for i in range(l-2, -1, -1):
#     for j in range(1,nums[i]+1):
#         jump = i + j
#         if jump < l:
#             dp[i] = min(dp[i], 1+dp[jump])
# print(dp[0])

#Greedy
r = c = l = 0
for i in range(len(nums)-1):
    r = max(r, i+nums[i])
    if i == l:
        l = r
        c += 1
print(c)
