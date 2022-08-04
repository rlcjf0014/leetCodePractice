class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        i = 1
        while i < len(nums):
            while nums[i] <= nums[i-1]:
                difference = (nums[i-1] - nums[i] + 1)
                nums[i]+= difference
                output+= difference
            i+=1
        return output
        