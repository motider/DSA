class Solution(object):
    def separateDigits(self, nums):
        new = []
        for i in nums:
            x = str(i)
            y = list(x)
            for j in y:
                new.append(int(j))
        return new
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        