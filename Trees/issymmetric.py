import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Trees import createtree, TreeNode 

from collections import deque

#treevals = [1,2,2,None,3,None,3]
treevals = [2,3,3,4,5,5,4,None,None,8,9,None,None,9,8]
root = createtree(treevals)
d = deque()
d.append((root, "c"))
flag = True
while len(d) > 0 and flag==True:
    fixed_length = len(d)
    for i in range(fixed_length):
        node, _ = d.popleft()
        if node == 0:
            continue
        if node.left:
            d.append((node.left, "l"))
        else:
            d.append((0, "l"))
        if node.right:
            d.append((node.right, "r"))
        else:
            d.append((0, "r"))
    k = len(d)
    if k%2 == 1:
        flag = False
        break
    for i in range(k//2):
        node1, b1 = d[i]
        node2, b2 = d[k-1-i]
        if node1 == 0 and node2 == 0 and b1!=b2:
            continue
        if node1 == 0 or node2 == 0 or (node1 == 0 and node2 == 0 and b1==b2):
            flag = False
            continue
        if node1.val != node2.val or b1==b2:
            flag = False
print(flag)
