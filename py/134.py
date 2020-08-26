## https://blog.csdn.net/james_154_best/article/details/80215687

class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        start, total, Min = 0, 0, sys.maxsize
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < Min:
                start = (i + 1)%len(gas)
                Min = total
        return start