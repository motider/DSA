class Solution(object):
    def maxPower(self, s):
        maxim = 1
        length = 1

        for r in range(1, len(s)):
            if s[r] == s[r-1]:
                length += 1
                maxim = max(maxim, length)
            else:
                length = 1
                
        return maxim  
        """
        :type s: str
        :rtype: int
        """
        