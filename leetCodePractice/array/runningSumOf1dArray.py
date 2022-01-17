class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for numIndex in range(1,len(nums)):
            nums[numIndex]=nums[numIndex]+nums[numIndex-1]
        return nums