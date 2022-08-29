class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) < 3:
            return sum(cost)
        
        cost.sort(reverse=True)
        
        result = 0
        while len(cost):
            first = cost.pop(0)
            result += first
            if len(cost):
                second = cost.pop(0)
                result += second
                if len(cost):
                    cost.pop(0)
        return result
            