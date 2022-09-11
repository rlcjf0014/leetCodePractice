class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCount = 0
        tempNum = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                tempNum += 1
            else:
                maxCount = max(maxCount, tempNum)
                tempNum = 0
            i+=1
        maxCount = max(maxCount, tempNum)
        return maxCount
        