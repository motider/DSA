class Solution(object):
    def removeDuplicates(self, nums):
        l = 0
        while l < len(nums):
            if nums.count(nums[l]) > 2:
                del nums[l]
            elif nums.count(nums[l]) == 2:
                l+=2
            else:
                l+=1
        return len(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        