class Solution(object):
    def reductionOperations(self, nums):
        nums.sort() 

        l = 0
        counter = 0
        while l < len(nums) - 1:
            if nums[l] != nums[l+1]:

                counter += (len(nums) - 1 - l)
            l += 1

        return counter

        """
        :type nums: List[int]
        :rtype: int
        """
        