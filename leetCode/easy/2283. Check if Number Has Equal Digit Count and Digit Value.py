class Solution(object):
    def digitCount(self,num):
        i = 0
        while i < len(num):
            if num.count(str(i)) != int(num[i]):
                return False
            i += 1
        return True
