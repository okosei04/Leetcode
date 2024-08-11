# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if root is None:
                return []

            return inorder(root.left) + [root] + inorder(root.right)

        nodes = inorder(root)
        first = second = None
        for i in range(len(nodes)-1):
            if nodes[i].val > nodes[i+1].val:
                second = nodes[i+1]
                if not first:
                    first = nodes[i]
                else:
                    break

        
        first.val, second.val = second.val,first.val


                
