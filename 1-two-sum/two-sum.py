class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        lists = []
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    lists.append(i)
                    lists.append(j)
        return lists

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        