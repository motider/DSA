class Solution(object):
    def transformArray(self, nums):
        x = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                x.append(0)
            else:
                x.append(1)
        x.sort()
        return x
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        