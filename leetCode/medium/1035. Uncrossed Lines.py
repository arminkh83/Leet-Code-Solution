def maxUncrossedLines(nums1, nums2):
    n1, n2 = len(nums1), len(nums2)
    currentRow, prevRow = [0] * (n2 + 1), [0] * (n2 + 1)
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if nums1[i - 1] == nums2[j - 1]:
                currentRow[j] = 1 + prevRow[j - 1]
            else:
                currentRow[j] = max(currentRow[j - 1], prevRow[j])
        prevRow = currentRow[:]
    return currentRow[n2]


print(maxUncrossedLines([3, 2], [2, 2, 2, 3]))
# class Solution(object):
#     pass
