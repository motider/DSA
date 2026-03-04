class Solution(object):
    def createTargetArray(self, nums, index):
        arr = []
        for i in range(len(nums)):
            arr.insert(index[i],nums[i])
        return arr
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        