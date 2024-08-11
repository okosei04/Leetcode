# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(root, isLeft):
            if root is None:
                return []
            
            curr = [root.val]
           

            left = dfs(root.left, True)
            right = dfs(root.right, False) 
            

            return left + curr + right

        return dfs(root, True)


            
        
        