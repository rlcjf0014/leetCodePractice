class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        leftMult = 1
        rightMult = 1
        for i in range(len(nums)-1, -1, -1):
            output.insert(0, rightMult)
            rightMult *= nums[i]

        for j in range(len(nums)):
            output[j] *= leftMult
            leftMult *= nums[j]


        return output
