class Solution(object):
    def pivotIndex(self, nums):
        for i in range(len(nums)):
            y = sum(nums[:i])
            z = sum(nums[i+1:len(nums)])
            if y == z:
                return i
                break
        else:
            return -1
        """
        :type nums: List[int]
        :rtype: int
        """
