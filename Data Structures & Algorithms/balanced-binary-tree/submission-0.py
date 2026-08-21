# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def dfs(node):
            if not node: return [True, 0]
    
            l, lh = dfs(node.left)
            r, rh = dfs(node.right)


            if l == False or r == False:
                return [False, max(lh, rh) + 1]
            
            # calculate the 
            if abs(rh-lh) > 1:
                return [False, max(lh, rh) + 1]
            else:
                return [True, max(lh, rh) + 1]


        return dfs(root)[0]






        