class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()

        n = len(nums)
        r = n - 1

        option1 = nums[r] * nums[r-1] * nums[r-2]

        option2 = nums[0] * nums[1] * nums[r]

        if option1 > option2:
            maxm = option1
        else:
            maxm = option2

        return maxm
        """
        :type nums: List[int]
        :rtype: int
        """
        