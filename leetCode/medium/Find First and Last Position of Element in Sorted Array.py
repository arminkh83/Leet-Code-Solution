def binary_Search(target, inputs):
    up, down = len(inputs) - 1, 0
    while up >= down:
        mid = (up + down) // 2
        if target > inputs[mid]:
            down = mid + 1
        elif target < inputs[mid]:
            up = mid - 1
        else:
            return mid
    return -1


def expand(place, inputs):
    if place < 0:
        return [-1, -1]

    down = up = place
    while down >= 0 and inputs[down] == inputs[place]:
        down -= 1
    while up < len(inputs) and inputs[up] == inputs[place]:
        up += 1
    return [down + 1, up - 1]


# class Solution(object):
def searchRange(nums, target):
    place = binary_Search(target, nums)
    return expand(place, nums)


print(searchRange([1], 1))
