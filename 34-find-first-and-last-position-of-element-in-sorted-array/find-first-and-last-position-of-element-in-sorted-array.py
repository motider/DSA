class Solution(object):
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        x = []
        for index, i in enumerate(nums):
            if i == target:
                x.append(index)  

            if target > i:
                left += 1  
            if target < i:
                right -= 1  

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
        