class Solution(object):
    def longestOnes(self, nums, k):
        l = 0
        zero = 0
        maxim = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero +=1
                
            while zero > k:
                if nums[l] == 0:
                    zero-=1
                    
                l+=1
                
            cur_wind = r-l+1
            maxim = max(maxim,cur_wind)
        return maxim
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        