class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        x = set(nums1)
        y = set(nums2)
        z = x & y   
        if z:   
            up = list(z)
            mini = min(up)
            return mini
        else:
            return -1

        