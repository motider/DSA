class Solution(object):
    def sortedSquares(self, nums):
        y =[x**2 for x in nums]
        y.sort()
        return y        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        