class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        return set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums1) & set(nums3)