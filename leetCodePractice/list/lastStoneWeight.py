class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            first = max(stones)
            stones.remove(first)
            second = max(stones)
            stones.remove(second)
            if first != second:
                new = first - second if first > second else second - first
                stones.append(new)
        return stones[0] if len(stones) == 1 else 0 
            