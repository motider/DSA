class Solution(object):
    def merge(self, nums1, m, nums2, n):
        l = 0
        r = 0
        x = []
        while l < m and r < n:
            if nums1[l] < nums2[r]:
                x.append(nums1[l])
                l += 1
            elif nums1[l] > nums2[r]:
                x.append(nums2[r])
                r += 1
            else:  
                x.append(nums1[l])
                x.append(nums2[r])
                l += 1
                r += 1

        x.extend(nums1[l:m])
        x.extend(nums2[r:n])

        nums1[:] = x  

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        