class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        newNums = list(set(nums))
        newNums.sort()

        result = 1
        length = 1
        for i in range(len(newNums) - 1):
            if abs(newNums[i] - newNums[i+1]) == 1:
                length += 1
            else:
                result = max(result, length)
                length = 1

        return max(result, length)

