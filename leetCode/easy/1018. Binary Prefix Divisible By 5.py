class Solution(object):
    def prefixesDivBy5(self, nums):
        numsLen = len(nums)
        res = [False] * numsLen
        res[0] = (nums[0] % 5 == 0)

        for i in range(1, numsLen):
            nums[i] = nums[i - 1] * 2 + nums[i]
            if nums % 5 == 0:
                res[i] = True
