class Solution(object):
    def findGCD(self, nums):
        x = max(nums)
        y = min(nums)

        new = []
        for i in range(1,y+1):
            if x % i == 0 and y % i == 0:
                new.append(i)
                
        return max(new)
        """
        :type nums: List[int]
        :rtype: int
        """
        