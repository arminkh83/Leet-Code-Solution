from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalTraversal(root):
    locations = deque()
    locations.append((0, 0, root))
    memory = [[0, 0, root]]
    cols = [0]
    while locations:
        row, col, node = locations.popleft()

        if bool(node.left):
            locations.append((row + 1, col - 1, node.left))
            memory += [[row + 1, col - 1, node.left]]
            if col - 1 not in cols:
                cols += [col - 1]

        if bool(node.right):
            locations.append((row + 1, col + 1, node.right))
            memory += [[row + 1, col + 1, node.right]]
            if col + 1 not in cols:
                cols += [col + 1]
    cols.sort()
    memory.sort(key=lambda x: (x[1], x[0], x[2].val))
    res = []
    place = 0
    for i in cols:
        addedToRes = []
        while place < len(memory) and memory[place][1] == i:
            addedToRes += [memory[place][2].val]
            place += 1
        res += [addedToRes]
    return res


root3 = TreeNode()
root9 = TreeNode()
# root20 = TreeNode()
# root15 = TreeNode()
# root7 = TreeNode()
root3.val = 3
root3.left = None
root3.right = root9
root9.val = 9
root9.left = None
root9.right = None
# root20.val = 20
# root20.left = root15
# root20.right = root7
# root15.val = 15
# root15.left = None
# root15.right = None
# root7.val = 7
# root7.left = None
# root7.right = None
#
print(verticalTraversal(root3))


# class Solution(object):
#     def verticalTraversal(root):
#         locations = deque()
#         locations.append((0, 0, root))
#         memory = [[0, 0, root]]
#         cols = []
#         while locations:
#             row, col, node = locations.popleft()
#
#             if bool(node.left):
#                 locations.append((row + 1, col - 1, node.left))
#                 memory += [[row + 1, col - 1, node.left]]
#                 if col - 1 not in cols:
#                     cols += [col - 1]
#
#             if bool(node.right):
#                 locations.append((row + 1, col + 1, node.right))
#                 memory += [[row + 1, col + 1, node.right]]
#                 if col + 1 not in cols:
#                     cols += [col + 1]
#         cols.sort()
#         memory.sort(key=lambda x: (x[1], x[0], x[2].val))
#         res = []
#         place = 0
#         for i in cols:
#             addedToRes = []
#             while place < len(memory) and memory[place][1] == i:
#                 addedToRes += [memory[place][2].val]
#                 place += 1
#             res += [addedToRes]
#         return res
