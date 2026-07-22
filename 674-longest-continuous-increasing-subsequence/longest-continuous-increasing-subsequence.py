class Solution(object):
    def findLengthOfLCIS(self, nums):
        maxim = 1
        length = 1

        for r in range(1, len(nums)):
            if nums[r] > nums[r-1]:
                length += 1
                maxim = max(maxim, length)
            else:
                length = 1
                
        return maxim  

        """
        :type nums: List[int]
        :rtype: int
        """
        