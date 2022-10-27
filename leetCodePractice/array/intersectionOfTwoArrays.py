class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        newNums1 = set(nums1)
        newNums2 = set(nums2)

        shorterNum = newNums1 if len(nums1) < len(nums2) else newNums2
        longerNum = newNums1 if len(nums1) > len(nums2) else newNums2

        result = []
        for num in shorterNum:
            if num in longerNum:
                result.append(num)

        return result