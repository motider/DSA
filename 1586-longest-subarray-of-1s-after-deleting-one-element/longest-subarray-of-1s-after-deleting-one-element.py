class Solution(object):
    def longestSubarray(self, nums):
        l = 0  
        zero_count = 0
        max_len = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1

            current_window_ones = r - l
            max_len = max(max_len, current_window_ones)

        return max_len
        """
        :type nums: List[int]
        :rtype: int
        """
        