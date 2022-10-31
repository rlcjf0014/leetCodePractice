class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        if len(nums) < 3:
            if nums[1] > nums[0]:
                return 1
            return 0

        l = 0
        i = 1
        r = 2

        while r < len(nums):
            if l == 0 and len(nums) == 3:
                if nums[l] > nums[i]:
                    return l
                if nums[r] > nums[i]:
                    return r

            if nums[i] > nums[l] and nums[i] > nums[r]:
                return i
            l+=1
            r+=1
            i+=1
        
        if nums[0] > nums[-1]:
            return 0
        else:
            return len(nums) - 1
            

        
