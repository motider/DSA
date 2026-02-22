class Solution(object):
    def containsDuplicate(self, nums):
        y = set(nums)
        if len(y) != len(nums):
            return True
        else:
            return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        