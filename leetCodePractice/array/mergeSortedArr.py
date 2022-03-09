class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        index1 = 0
        index2 = 0
        del nums1[m:]
        while m and n:
            if nums1[index1] < nums2[index2]:
                index1+=1
                m-=1
            else:
                nums1.insert(index1, nums2[index2])
                index1+=1
                index2+=1
                n-=1
                
        
        if n > 0:
            nums1.extend(nums2[index2::])