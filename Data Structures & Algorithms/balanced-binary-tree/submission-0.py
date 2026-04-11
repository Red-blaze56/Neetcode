# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True
            left = dfs(root.left)
            if left == -1:
                return -1
            right = dfs(root.right)
            if right == -1:
                return -1

            if abs(left-right) > 1:
                return -1
            
            return 1+max(left,right)
        w = dfs(root)
        return False if w==-1 else True
 
