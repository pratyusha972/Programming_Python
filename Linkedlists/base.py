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

def printlist(node):
    temp = node
    ans = []
    while temp!=None:
        ans.append(temp.val)
        temp = temp.next
    print(ans)

