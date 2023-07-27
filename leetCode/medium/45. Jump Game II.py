def videoStitching(clips, time):
    left = -1
    right = 0
    res = 0
    clips.sort(key= lambda x: (x[0], -x[1]))
    for i, j in clips:
        if right >= time or i > right:
            break
        elif left < i <= right:
            left = right
            res += 1
        right = max(right, j)
    return res if right >= time else -1


def createClips(nums):
    clips = []
    for i in range(len(nums)):
        clips += [[i, i + nums[i]]]
    return clips


def jumpBetter(nums):
    jump = cur = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur:
            jump += 1
            cur = farthest
    return jump


def jumpBetter2(nums):
    jump = cur = 0
    while cur < len(nums) - 1:
        x = [] +=  for i in range(cur+1:cur+nums[cur]+1)
        cur = max(x)
        jump += 1
    return jump


print(jumpBetter2([2,3,1,1,4]))


class Solution(object):
    def jump(self, nums):
        jump = cur = farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == cur:
                jump += 1
                cur = farthest
        return jump
