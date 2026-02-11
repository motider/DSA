class Solution(object):
    def findDifference(self, nums1, nums2):
        set1= set(nums1)
        set2= set(nums2)
        x = list(set1 - set2) 
        y = list(set2 - set1) 
        z = []
        z.append(x)
        z.append(y)

        return z
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        