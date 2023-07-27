from idlelib.tree import TreeNode


class Solution(object):
    def sortedArrayToBST(self, nums):
        arrayLen = len(nums)
        if not arrayLen:
            return None
        middleNodeIndex = arrayLen // 2
        middleNode = nums[middleNodeIndex]
        return TreeNode(
            nums[middleNode],
            self.sortedArrayToBST(nums[:middleNodeIndex]), self.sortedArrayToBST(nums[middleNodeIndex + 1:])
        )
