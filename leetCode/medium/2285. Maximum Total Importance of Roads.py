def findDeg(roads, n):
    degrees = [0] * n
    for i, j in roads:
        degrees[i], degrees[j] = degrees[i] + 1, degrees[j] + 1
    degrees.sort(reverse=True)
    return degrees


def maximumImportance( n: int, roads) -> int:
    degrees = findDeg(roads, n)
    totoalSum = 0
    for i in degrees:
        totoalSum += n * i
        n -= 1
    return totoalSum


print(maximumImportance(5,[[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]))


class Solution:
    pass
