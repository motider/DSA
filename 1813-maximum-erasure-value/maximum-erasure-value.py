class Solution(object):
    def maximumUniqueSubarray(self, nums):
        l = 0
        maps = {}
        maxim = 0
        current_sum = 0

        for r, num in enumerate(nums):
            if num in maps and maps[num] >= l:
                while l <= maps[num]:
                    current_sum -= nums[l]
                    l += 1
                
            maps[num] = r
            current_sum += num
            maxim = max(maxim, current_sum)
            
        return maxim

        """
        :type nums: List[int]
        :rtype: int
        """
        