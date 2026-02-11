class Solution(object):
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        l = 0
        r = 0
        x = []
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                l += 1
            elif nums1[l] > nums2[r]:
                r += 1
            else:
                if nums1[l] not in x:
                    x.append(nums1[l])
                l += 1
                r += 1

        return x
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        