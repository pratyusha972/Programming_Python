#problem: https://leetcode.com/problems/add-two-numbers/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createlist(l):
    head = ListNode(val=l[0])
    h1 = head
    for i in range(1,len(l)):
        h1.next = ListNode(l[i])
        h1 = h1.next
    return head

#example:
list1 = [9,9,9,9,9,9,9]
list2 = [9,9,9,9]

#l1 and l2 are linked lists
l1 = createlist(list1)
l2 = createlist(list2)

prev_val = 0
head = ListNode(val=0)
l3 = head
while True:
    if l1!=None and l2!=None:
        val = l1.val + l2.val + prev_val
        l1 = l1.next
        l2 = l2.next
    elif l1 == None and l2!=None:
        val = l2.val + prev_val
        l2 = l2.next
    elif l1!=None and l2==None:
        val = l1.val + prev_val
        l1 = l1.next
    prev_val = val//10
    l3.val = val%10
    if l1==None and l2==None:
        break
    else:
        l3.next = ListNode(val=0)
        l3 = l3.next
if prev_val == 1:
    l3.next = ListNode(val=1)

h4 = head
ans = []
while h4!=None:
    ans.append(h4.val)
    h4 = h4.next
print(ans)
