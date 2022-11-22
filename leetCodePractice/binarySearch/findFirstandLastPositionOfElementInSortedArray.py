class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
        
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] == target and nums[j] == target:
                return [i, j]
            if nums[i] < target:
                i+=1
            if nums[j] > target: 
                j-=1

        return [-1, -1]