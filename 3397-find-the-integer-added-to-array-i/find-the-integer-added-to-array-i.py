class Solution(object):
    def addedInteger(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        y = nums2[0] -nums1[0] 

        for i in range(len(nums1)):
            if len(nums1) == len(nums2) and nums1[i] + y == nums2[i]:
                return y
                break
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        