import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from trees import createtree, TreeNode 

treevals = [1,2,3,4,5]
root = createtree(treevals)

max_h = 0
def recur(node):
    global max_h
    if node == None:
        return 0
    left_h = recur(node.left)
    right_h = recur(node.right)
    max_h = max(max_h, left_h + right_h)
    return max(left_h, right_h) + 1
_ = recur(root)
print(max_h)
