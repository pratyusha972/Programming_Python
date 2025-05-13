import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createlist(l):
    head = ListNode(val=l[0])
    h = head
    for i in range(1,len(l)):
        h.next = ListNode(l[i])
        h = h.next
    return head

#example:
h1 = [18,6,10,3]
head = createlist(h1)

temp = head
while temp.next!=None:
    newnode = ListNode(math.gcd(temp.val, temp.next.val), temp.next)
    temp.next = newnode
    temp = newnode.next

h = head
ans = []
while h!=None:
    ans.append(h.val)
    h = h.next
print(ans)
