# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        if not bool(root):
            return []
        nodes, res = deque(root), []
        while nodes:
            depthCount = len(nodes)
            temp = []
            for i in range(depthCount):
                curNode = nodes.popleft()
                temp += curNode.val
                if curNode.left:
                    nodes.append(root.left)
                if curNode.right:
                    nodes.append(root.right)
            res += [temp]
        return res