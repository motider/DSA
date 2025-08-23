class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = []
        x = min(len(nums1),len(nums2))
        for i in nums1:
            if i in nums2:   
                nums.append(i)
                nums2.remove(i)   
        return nums

        