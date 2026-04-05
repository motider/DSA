class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)

        if n % 2 == 0:
            x = nums1[n//2] + nums1[n//2-1]
            return x / 2.0
        else:
            return nums1[(n//2)]
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        