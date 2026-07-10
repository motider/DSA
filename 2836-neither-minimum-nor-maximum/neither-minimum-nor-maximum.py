class Solution(object):
    def findNonMinOrMax(self, nums):
        unique_nums = list(set(nums))
        unique_nums.sort()

        if len(unique_nums) < 3:
            return -1
        else:
            return unique_nums[-2]
        """
        :type nums: List[int]
        :rtype: int
        """
        