# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return root
        
        node = deque([root])

        while node:
            v = node.popleft()

            
            v.left, v.right = v.right, v.left

            if v.left:
                node.append(v.left)
            
            if v.right:
                node.append(v.right)

            
        return root