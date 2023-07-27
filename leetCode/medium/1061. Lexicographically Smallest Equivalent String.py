UF = {}


def find(x):
    UF.setdefault(x, x)
    if x != UF[x]:
        UF[x] = find(UF[x])
    return UF[x]


def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX > rootY:
        UF[rootX] = rootY
    else:
        UF[rootY] = rootX


# class Solution(object):
def smallestEquivalentString(s1, s2, baseStr):
    for i in range(len(s1)):
        union(s1[i], s2[i])
    res = []
    for character in baseStr:
        res.append(find(character))
    return ''.join(res)

# print(smallestEquivalentString("hello","world","hold"))
