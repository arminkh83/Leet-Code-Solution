# def minNonZeroProduct(p):


# print(minNonZeroProduct(3))


class Solution(object):
    def minNonZeroProduct(self, p):
        a = 2 ** p

        return (int(pow(2**p -2, 2**(p-1) - 1, 10**9 + 7) ) * (a - 1)) % (10**9 + 7)
