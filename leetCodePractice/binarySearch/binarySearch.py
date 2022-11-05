class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
            

        l, r = 0, len(nums) - 1

        while l != r and l < r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r

            half = (l+r) // 2
            if target == nums[half]:
                return half
            elif target > nums[half]:
                l = half
                l+=1
            else:
                r = half
                r-=1

        return -1

                
                