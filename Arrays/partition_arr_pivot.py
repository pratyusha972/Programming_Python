nums = [-3,4,3,2]
pivot = 2
index = 0
count = 0
length = len(nums)
temp_end = length - 1
flag = False
while count < length:
    if nums[index] > pivot:
        temp = nums.pop(index)
        if flag == False:
            temp_end = length-2
            flag = True
        else:
            temp_end -= 1
        nums.append(temp)
    elif nums[index] == pivot:
        temp1 = nums.pop(index)
        nums.insert(temp_end, pivot)
    else:
        index += 1
    count += 1
print(nums)
