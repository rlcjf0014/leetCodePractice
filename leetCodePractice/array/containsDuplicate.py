class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Converting to set removes duplicates
        return False if len(nums) == len(set(nums)) else True
        