class Solution(object):
    def countElements(self, nums):
        nums.sort()
        new = []
        for i in nums:
            if i != min(nums) and i != max(nums):
                new.append(i)
                
        return len(new)
        
        """
        :type nums: List[int]
        :rtype: int
        """
        