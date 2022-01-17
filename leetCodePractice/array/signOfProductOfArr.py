class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 in nums:
            return 0
        negNumFreq=0
        for num in nums:
            if num < 0:
                negNumFreq+=1
        return -1 if negNumFreq % 2 == 1 else 1