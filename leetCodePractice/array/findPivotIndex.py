class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumSoFar = 0
        for i in range(len(nums)):
            if sum(nums[i+1:]) == sumSoFar:
                return i
            sumSoFar += nums[i]
        return -1