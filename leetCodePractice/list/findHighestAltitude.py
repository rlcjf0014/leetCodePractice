class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current = 0
        result = [0]
        for number in gain:
            current += number
            result.append(current)
        
        return max(result)