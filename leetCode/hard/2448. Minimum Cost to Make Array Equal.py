import math


class Solution:
    def minCost(nums, cost) -> int:
        def getCost(x):
            return sum(abs(x - i) * j for i, j in zip(nums, cost))

        def getClosest(target_value):
            return min(nums, key=lambda x: abs(target_value - x))

        left, right = min(nums), max(nums)
        answer = 0
        while left < right:
            mid = (left + right) // 2
            midCost = getCost(getClosest(mid))
            midCost2 = getCost(getClosest(mid + 1))

            answer = min(midCost, midCost2)
            if midCost > midCost2:
                left = mid + 1
            else:
                right = mid
