class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]

        cur = 1
        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * cur
            cur *= nums[i]

        return answer
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        