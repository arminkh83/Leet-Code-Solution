class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        num = len(bookings) + 1
        res = [0] * num
        for i, j, k in bookings:
            res[i - 1] += k
            res[j] -= k
        for i in range(1, num):
            res[i] += res[i-1]
        return res[:num-1]