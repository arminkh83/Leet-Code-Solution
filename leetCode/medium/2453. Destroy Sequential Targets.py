from collections import Counter


class Solution(object):
    def destroyTargets(nums, space):
        count = Counter(item % space for item in nums)
        mostFrequent = max(count.values())
        return min(a for a in nums if count[a % space] == mostFrequent)
