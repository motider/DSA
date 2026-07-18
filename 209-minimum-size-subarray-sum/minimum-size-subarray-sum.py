class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        current_sum = 0
        min_len = len(nums) + 1

        for r in range(len(nums)):
            current_sum += nums[r]

            while current_sum >= target:
                min_len = min(min_len, r - l + 1)
                current_sum -= nums[l]
                l += 1

        result = min_len if min_len <= len(nums) else 0
        return result
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        