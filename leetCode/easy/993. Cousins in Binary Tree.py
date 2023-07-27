from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    @staticmethod
    def isCousins(self, root, x, y):
        depth = 0
        depthX, depthY = -1, -1

        depths = deque()
        depths.append((root, 0))

        while len(depths) > 0 and (depthX == -1 or depthY == -1):
            curNode, curDepth = depths.popleft()
            if curDepth.value == x:
                depthX = curDepth
            elif curDepth.value == y:
                depthY = curDepth
            if bool(curNode.left):
                depths.append((curNode.left, curDepth + 1))
            elif bool(curNode.right):
                depths.append((curNode.right, curDepth + 1))

        return depthX == depthY
