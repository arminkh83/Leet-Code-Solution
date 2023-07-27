class Solution:
    def minGroups(intervals: list[list[int]]) -> int:
        def removeSubset(subset):
            for i, j in subset:
                intervals.remove([i, j])
                
        intervals.sort()
        marked = [0] * len(intervals)
        left, right = -2, -1
        group = 0
        while intervals:
            group += 1
            left, right = -1, 0
            subset = []
            for i, j in intervals:
                if i <= right:
                    continue
                right = j
                subset += [[i, j]]
            removeSubset(subset)

        return group


# print(minGroups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]))
#     pass
