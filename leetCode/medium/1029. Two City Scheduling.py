class Solution(object):
    def twoCitySchedCost(self, costs):
        sum = 0
        benefit = []
        for [i, j] in costs:
            sum += i
            benefit += [j - i]
        benefit.sort()
        for i in benefit[:len(benefit) // 2]:
            sum += i
        return sum
