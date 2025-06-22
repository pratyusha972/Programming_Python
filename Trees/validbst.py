#Problem: https://leetcode.com/problems/validate-binary-search-tree/
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Trees import createtree, TreeNode 


treevals = [5,4,6,None,None,3,7]
root = createtree(treevals)

def check(node, left, right):
    if node == None:
        return True
    if node.val <= left or node.val >= right:
        return False
    check1 = check(node.left, left, node.val)
    check2 = check(node.right, node.val, right)
    return check1 and check2
print(check(root, float('-inf'), float('inf')))
