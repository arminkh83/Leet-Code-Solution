def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: (x[1]))
    curEnd = intervals[0][1]
    removeCount = 0
    for i, j in intervals[1:]:
        if i < curEnd:
            removeCount += 1
            continue
        curEnd = j
    return removeCount


print(eraseOverlapIntervals(
    [[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95], [-31, 49], [66, 98], [-63, 2],
     [30, 47], [-40, -26]]))
# class Solution(object):
