def sortBasedOnStartTime(e):
    return e[0]


def sortBasedOnEndTime(e):
    return e[1]


# class Solution(object):


def videoStitching(clips, time):
    prev_end, end, cnt = -1, 0, 0
    for i, j in sorted(clips):
        if i > end or end >= time:
            break
        if prev_end < i <= end:
            prev_end, cnt = end, cnt + 1
        end = max(end, j)
    return cnt if end >= time else -1


print(videoStitching([[0,2],[4,8]], 5))
