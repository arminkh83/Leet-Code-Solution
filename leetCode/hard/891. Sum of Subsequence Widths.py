class Solution:
    def sumSubseqWidths(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)

        return sum(nums[i] * (2 ** i - 2 ** (n - i - 1)) for i in range(n))
