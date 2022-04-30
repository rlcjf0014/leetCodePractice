class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = len(nums) / 2
        for num in nums:
            if nums.count(num) == times:
                return num