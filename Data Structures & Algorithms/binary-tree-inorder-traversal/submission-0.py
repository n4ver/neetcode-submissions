# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Left, Root, Right
        if not root: return []
        # return [root.left.val, root.val, root.right.val]
        res = []
        res.extend(self.inorderTraversal(root.left))
        res.extend([root.val])
        res.extend(self.inorderTraversal(root.right))
        return res
