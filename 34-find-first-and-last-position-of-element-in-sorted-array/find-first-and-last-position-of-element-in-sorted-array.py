class Solution(object):
    def searchRange(self, nums, target):
        low = 0
        high = len(nums) - 1
        x = []
        for index, i in enumerate(nums):
            if i == target:
                x.append(index)  

            if target > i:
                low += 1  
            if target < i:
                high -= 1  

        if x:
            result = [x[0], x[-1]]
        else:
            result = [-1, -1]

        return result 
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        