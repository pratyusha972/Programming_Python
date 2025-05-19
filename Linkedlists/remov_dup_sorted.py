#problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
from base import createlist, printlist, ListNode
head = createlist([1,1,2,2,3,3,3])
temp = head
while temp!=None:
    if temp.next!=None:
        if temp.val!=temp.next.val:
            temp = temp.next
        else:
            temp.next = temp.next.next
    else:
        temp = temp.next
printlist(head)
