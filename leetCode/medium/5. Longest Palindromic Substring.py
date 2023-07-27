class Solution(object):
    def longestPalindrome(self, s):
        result = ""
        for i in range(len(s)):
            result = max(result, expand(s, i, i), expand(s, i, i + 1), key=len)
        return result


def expand(s: str, down, up):
    while down >= 0 and up < len(s) and s[down] == s[up]:
        down -= 1
        up += 1
    return s[down + 1:up]
