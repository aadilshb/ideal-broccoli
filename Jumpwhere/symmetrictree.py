class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def are_symmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
    else:
        return are_symmetric(root1.left, root2.right) and are_symmetric(root1.right, root2.left)

def is_symmetric(root):
    if root is None:
        return True
    return are_symmetric(root.left, root.right)
root1=TreeNode(5,TreeNode(2,TreeNode(9,TreeNode(3),TreeNode(0)),TreeNode(7,TreeNode(6))),TreeNode(8,TreeNode(1)))
root2=TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(2,TreeNode(4),TreeNode(3)))
print(is_symmetric(root1))
print(is_symmetric(root2)) 