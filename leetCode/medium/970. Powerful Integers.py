def powerfulIntegers(x: int, y: int, bound: int) -> list[int]:
    i = 0
    res = []
    while y ** i <= bound:
        j = 0
        while x ** j + y ** i <= bound:
            if x ** j + y ** i not in res and x == 1:
                res += [x ** j + y ** i]
                break
            j += 1
        i += 1
    res.sort()
    return res


print(powerfulIntegers(2, 3, 10))
# class Solution:
# pass
