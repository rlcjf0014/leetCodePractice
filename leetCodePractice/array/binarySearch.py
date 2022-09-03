class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] == target:
            return 0
        
        i = 0
        end = len(nums) - 1
        
        
        while i <= end:
            if nums[i] == target:
                return i
            if nums[end] == target:
                return end
            i+=1
            end-=1
            
        return -1