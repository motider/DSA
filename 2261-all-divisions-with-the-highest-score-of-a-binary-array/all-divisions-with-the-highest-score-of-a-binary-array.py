class Solution(object):
    def maxScoreIndices(self, nums):
        zeros = 0
        ones = nums.count(1)
        new = [zeros + ones]
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                ones -= 1
            new.append(zeros + ones)

        max_val = max(new)
        fin = [idx for idx, val in enumerate(new) if val == max_val]
        return fin
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        