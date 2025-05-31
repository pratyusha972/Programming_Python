#Problem:https://leetcode.com/problems/intersection-of-two-arrays/
nums1 = [1,2,2,1]
nums2 = [2,2]
a = set()
b = set()
for i in range(len(nums1)):
    a.add(nums1[i])
for j in range(len(nums2)):
    b.add(nums2[j])
print(list(a.intersection(b)))
