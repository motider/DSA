class Solution(object):
    def findMiddleIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        for i,val in enumerate(nums):
            if left_sum == (total_sum - left_sum - val):
                return i
                break
            left_sum+=val
        else:
            return -1
        """
        :type nums: List[int]
        :rtype: int
        """
        