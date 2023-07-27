def createRanges(nums):
    res = []
    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        res += [[max(0, i - nums[i]), i + nums[i]]]
    res.sort()
    return res


def videoStitching(clips, time):
    prev_end, end, cnt = -1, 0, 0
    for i, j in clips:
        if i > end or end >= time:
            break
        if prev_end < i <= end:
            prev_end, cnt = end, cnt + 1
        end = max(end, j)
    return cnt if end >= time else -1


# print(createRanges([3, 4, 1, 1, 0, 0]))


class Solution(object):
    def minTaps(self, n, ranges):
        return videoStitching(createRanges(ranges), n)
