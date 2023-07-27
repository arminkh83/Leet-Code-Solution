import math


def average(inputs):
    if not inputs:
        return 0
    return sum(i for i in inputs) / len(inputs)


# print(minimumAverageDifference([4, 2, 0]))
class Solution(object):
    def minimumAverageDifference(nums):
        numsLen = len(nums)
        if numsLen == 1:
            return 0
        totalSum = sum(a for a in nums)
        tempSum = 0
        min_avg =
        leftPartAvg = 0
        rightPartAvg = 0
        index = -1
        for i in range(numsLen):
            tempSum += nums[i]
            leftPartAvg = tempSum // (i + 1)
            if numsLen - i - 1 != 0:
                rightPartAvg = (totalSum - tempSum) // (numsLen - i - 1)
            else:
                rightPartAvg = 0

            diff = abs(leftPartAvg - rightPartAvg)
            if diff < min_avg:
                min_avg = diff
                index = i
        return index
