class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for x in nums:
            if nums.count(x) % 2 != 0:
                return False
        return True