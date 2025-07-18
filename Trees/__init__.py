class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createtree(l):
    def recur(l, ind):
        node = TreeNode(val=l[ind])
        if len(l) <= 2*ind+2:
            return node
        if l[2*ind+1] != None:
            node.left = recur(l, 2*ind+1)
        if l[2*ind+2] != None:
            node.right = recur(l, 2*ind+2)
        return node
    return recur(l, 0)


def printtree(root):
    def inorder(node, ans):
        if node == None:
            return ans
        ans = inorder(node.left, ans)
        ans.append(node.val)
        ans = inorder(node.right, ans)
        return ans
    ans = inorder(root, [])
    print(ans)
