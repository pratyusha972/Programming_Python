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
h1 = [1,2,4]
h2 = [1,3,4]

#l1 and l2 are linked lists
list1 = createlist(h1)
list2 = createlist(h2)

list3 = None
if list1 == None:
    list3 = list2
elif list2 == None:
    list3 = list1
elif list1 == None and list2 == None:
    list3 = list1
else:
    temp1 = list1
    temp2 = list2
    list3 = ListNode(0)
    if list1.val >= list2.val:
        list3.val = list2.val
        temp2 = temp2.next
    else:
        list3.val = list1.val
        temp1 = temp1.next
    temp3 = list3
    while temp1!=None or temp2!=None:
        temp3.next = ListNode(0)
        temp3 = temp3.next
        if (temp1==None) or (temp2!=None and temp1.val >= temp2.val):
            temp3.val = temp2.val
            temp2 = temp2.next
        else:
            temp3.val = temp1.val
            temp1 = temp1.next

h3 = list3 
ans = []
while h3!=None:
    ans.append(h3.val)
    h3 = h3.next
print(ans)
