class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lowest = nums[0]
        for i in range(1, len(nums)):
            compare = abs(0 - lowest)
            target = abs(0 - nums[i])
            if target < compare:
                lowest = nums[i]
            elif target == compare:
                lowest = nums[i] if nums[i] > lowest else lowest
            else:
                continue
        return lowest