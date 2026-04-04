class Solution(object):
    def singleNumber(self, nums):
        new = []
        for i in nums:
            if nums.count(i) == 1:
                new.append(i)
        return new
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        