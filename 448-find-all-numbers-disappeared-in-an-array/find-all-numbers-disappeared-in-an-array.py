class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums_set = set(nums) 
        y = []

        for i in range(1, len(nums) + 1):
            if i not in nums_set: 
                y.append(i)
        return y

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        