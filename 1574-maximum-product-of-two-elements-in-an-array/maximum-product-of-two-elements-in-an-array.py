class Solution(object):
    def maxProduct(self, nums):
        nums.sort()
        new =[]
        for i in range(len(nums)-1):
            y = (nums[i]-1) * (nums[i+1]-1)
            new.append(y)
        return max(new)
        """
        :type nums: List[int]
        :rtype: int
        """
        