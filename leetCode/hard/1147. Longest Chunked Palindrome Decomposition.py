

# print(longestDecomposition("ghiabcdefhelloadamhelloabcdefghi"))


class Solution(object):
    def longestDecomposition(text):
        textLen = len(text)
        i = 1
        pair = 0
        leftWall = 0
        rightWall = textLen
        while i <= textLen - i:
            print(text)
            print(text[: i], text[- i:])
            if text[: i] == text[- i:]:
                text = text[i:-i]
                textLen = len(text)
                print(text)
                i = 1
                pair += 2
            else:
                i += 1
        if text:
            pair += 1
        return pair

