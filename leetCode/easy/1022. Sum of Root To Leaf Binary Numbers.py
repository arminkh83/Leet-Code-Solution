# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def sumRootToLeaf(self, root, value=0):
        if not root:
            return 0
        value = value * 2 + root.val
        if not bool(root.left) and not bool(root.right):
            return value
        return self.sumRootToLeaf(root.left, value) + self.sumRootToLeaf(root.right, value)
