class Solution(object):
    def lengthOfLastWord(self, s):
        y = s.split()
        n = len(y)
        x = len(y[n-1])
        return x
        """
        :type s: str
        :rtype: int
        """
        