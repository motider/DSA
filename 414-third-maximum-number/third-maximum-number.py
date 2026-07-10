class Solution(object):
    def thirdMax(self, nums):
        unique_nums = list(set(nums))
        unique_nums.sort()
        
        if len(unique_nums) < 3:
            return unique_nums[-1]  
        else:
            return unique_nums[-3]
        """
        :type nums: List[int]
        :rtype: int
        """
        