from bisect import bisect_left, bisect_right





# print(fullBloomFlowers([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11]))


class Solution(object):
    def fullBloomFlowers(flowers, people):
        flowers.sort(key=lambda x: (x[0], x[1]))
        start, end = [a for a, b in flowers], [b for a, b in flowers]
        return [bisect_right(start, t) - bisect_left(end, t) for t in people]
