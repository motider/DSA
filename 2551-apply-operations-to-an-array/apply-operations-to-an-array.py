class Solution(object):
    def applyOperations(self, nums):
        l = 0 
        r = 1
        x = []

        while r < len(nums):
            if nums[l] == nums[r]:
                x.append(nums[l] * 2)
                x.append(0)
                l += 2 
                r += 2
            else:
                x.append(nums[l])
                l += 1 
                r += 1

        if l < len(nums):
            x.append(nums[l])
        l = 0
        r = 0
        while r < len(x):
            if x[r] != 0:
                x[l], x[r] = x[r], x[l]
                l += 1
            r += 1

        return x
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        