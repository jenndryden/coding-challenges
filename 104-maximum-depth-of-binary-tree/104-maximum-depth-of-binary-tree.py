# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        tracker = []
        depth = 0
        if not root: return 0
        def depth_check(node, depth):
            if node:
                depth += 1
                if not node.right and not node.left:
                    tracker.append(depth)
                    depth = 0
                depth_check(node.right, depth)
                depth_check(node.left, depth)
        
        depth_check(root, 0)
        return max(tracker)
            