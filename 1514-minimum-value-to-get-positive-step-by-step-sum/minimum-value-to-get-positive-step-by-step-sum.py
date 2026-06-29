class Solution(object):
    def minStartValue(self, nums):
        running_sum = 0
        min_running_sum = 0
        for num in nums:
            running_sum += num
            if running_sum < min_running_sum:
                min_running_sum = running_sum
                
        return 1 - min_running_sum

        """
        :type nums: List[int]
        :rtype: int
        """
        