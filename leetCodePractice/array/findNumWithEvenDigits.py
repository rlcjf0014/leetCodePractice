class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for x in nums:
            if len(str(x)) % 2 == 0:
                result+=1
        return result