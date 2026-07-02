class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        nums.sort()
        
        freq = {}
        curr = nums[0]
        freq[curr] = 1
        
        for i in range(1, len(nums)):
            if nums[i] == curr:
                continue
                
            if nums[i] == curr + 1:
                freq[curr] += 1
                freq[nums[i]] = freq.pop(curr)
            else:
                freq[nums[i]] = 1
                
            curr = nums[i]
            
        return max(freq.values())


        """
        :type nums: List[int]
        :rtype: int
        """
        