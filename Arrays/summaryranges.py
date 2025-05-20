nums = [1,2,4,5,7,8]
if len(nums) == 0:
    print([])
elif len(nums) == 1:
    print([str(nums[0])])
else:
    start = 0
    ans = []
    end = None
    for i in range(len(nums)-1):
        if nums[i] + 1 != nums[i+1]:
            if end == None:
                ans.append(str(nums[start]))
            else:
                ans.append(str(nums[start]) + "->" + str(nums[end]))
            end = None
            start = i + 1
        else:
            end = i+1
    if end == None and start == (len(nums) - 1):
        ans.append(str(nums[start]))
    elif end != None:
        ans.append(str(nums[start]) + "->" + str(nums[end]))
    print(ans)
