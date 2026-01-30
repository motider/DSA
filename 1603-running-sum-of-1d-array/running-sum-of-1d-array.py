class Solution(object):
    def runningSum(self, nums):
        x = []
        r = len(nums)-1
        for i in range(len(nums)):
            y = sum(nums)
            x.append(y)
            nums.pop()
        z = x[::-1]
        return z
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        