class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum = 0
        for x in nums:
            if nums.count(x) == 1:
                sum+=x
        return sum