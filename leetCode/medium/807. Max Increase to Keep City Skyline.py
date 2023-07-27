def findMaxByItsCul(grid, cul):
    res = []
    for i in range(len(grid)):
        res += [grid[i][cul]]
    return max(res)


def maxIncreaseKeepingSkyline(grid):
    row, col = map(max, grid), map(max, zip(*grid))
    return sum(min(i, j) for i in row for j in col) - sum(map(sum, grid))


print(maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))

# class Solution(object):
#     def maxIncreaseKeepingSkyline(grid):
#         step = 0
#         for i in range(len(grid)):
#             rowMax = max(grid[i])
#             for j in range(len(grid)):
#                 culMax = findMaxByItsCul(grid, j)
#                 step += abs(min(rowMax, culMax) - grid[i][j])
#         return step
