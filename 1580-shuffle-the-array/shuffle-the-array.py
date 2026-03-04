class Solution(object):
    def shuffle(self, nums, n):
        nums1 = nums[:n]
        nums2 = nums[n:]

        new = []
        l = 0
        r = 0
        while r < n:
            new.append(nums1[l])
            new.append(nums2[r])
            l+=1
            r+=1
        return new
    
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        