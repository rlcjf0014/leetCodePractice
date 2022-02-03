class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = nums
        for i in range(len(nums)):
            result.append(nums[i])
        return result