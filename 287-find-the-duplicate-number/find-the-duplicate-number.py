class Solution(object):
    def findDuplicate(self, nums):
        x = set() 
        for i in nums:
            if i in x:
                return i
                break
            x.add(i)
        """
        :type nums: List[int]
        :rtype: int
        """
        