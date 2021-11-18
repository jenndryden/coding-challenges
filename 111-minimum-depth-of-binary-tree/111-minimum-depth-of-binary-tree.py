# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depths = []
        depth = 0 
        
        if not root: return 0
        def min_depth(node, depth):
            if node:
                depth += 1
                min_depth(node.right, depth)
                min_depth(node.left, depth)
                if not node.left and not node.right:
                    depths.append(depth)
                    depth  = 0
        min_depth(root, 0)
        return min(depths)
        