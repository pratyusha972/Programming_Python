import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Trees import createtree, TreeNode, printtree

nums = [-10,-3,0,5,9]
def make(array): 
    if len(array) == 0:
        return None
    mid = len(array)//2
    newnode = TreeNode(array[mid], make(array[:mid]), make(array[mid+1:]))    
    return newnode
    
root = make(nums)
printtree(root)
