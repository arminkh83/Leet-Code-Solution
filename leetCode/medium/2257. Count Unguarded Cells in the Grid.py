def fillGuards(grid, cord):
    for i, j in cord:
        grid[i][j] = 2


direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]


class Solution(object):
    def countUnguarded(m, n, guards, walls):
        grid = [[0] * n for i in range(m)]
        fillGuards(grid, guards + walls)
        for i, j in guards:
            for dx, dy in direction:
                newX, newY = i + dx, j + dy
                while 0 <= newX < m and 0 <= newY < n and grid[newX][newY] != 2:
                    grid[newX][newY] = 1
                    newX, newY = newX + dx, newY + dy

        return sum(row.count(0) for row in grid)