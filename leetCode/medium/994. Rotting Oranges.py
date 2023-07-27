from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




# root1 = TreeNode()
# root2 = TreeNode()
# root3 = TreeNode()
# root4 = TreeNode()
# root5 = TreeNode()
#
# root1.val = 1
# root1.left = root2
# root1.right = root3
# root2.val = 2
# root2.left = None
# root2.right = root4
# root3.val = 3
# root3.left = None
# root3.right = root5
# root4.val = 4
# root4.left = None
# root4.right = None
# root5.val = 5
# root5.left = None
# root5.right = None


# print(isCousins(root1,4,5))


class Solution(object):
    def isCousins( root, x, y):
        depthX, depthY = -1, -1
        details = [[-1, root.val], [-1, root.val]]
        depths = deque()
        depths.append((root, 0, root.val))

        while len(depths) > 0 and (depthX == -1 or depthY == -1):
            curNode, curDepth, parentValue = depths.popleft()
            if curNode.val == x:
                depthX = curDepth
                details[0][0] = depthX
                details[0][1] = parentValue
            elif curNode.val == y:
                depthY = curDepth
                details[1][0] = depthY
                details[1][1] = parentValue
            if bool(curNode.left):
                depths.append((curNode.left, curDepth + 1, curNode.val))
            if bool(curNode.right):
                depths.append((curNode.right, curDepth + 1, curNode.val))
        return details[0][0] == details[1][0] and details[0][1] != details[1][1]













