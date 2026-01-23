class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        left = 0
        right = len(nums) -1
        x = []
        for index,i in enumerate(nums):
            if i == target:
                x.append(index)
            if i < target:
                left+=1
            if i > target:
                right-=1
        return x
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        