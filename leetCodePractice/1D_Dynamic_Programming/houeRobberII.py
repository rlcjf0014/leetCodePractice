class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robHelper(nums[1:]), self.robHelper(nums[:-1]))


    def robHelper(self, numsList):
        rob1, rob2 = 0, 0

        for n in numsList:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2