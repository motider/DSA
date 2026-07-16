class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        new = []
        for l in range(len(s)):
            x = ""
            x += s[l]

            for r in range(l + 1, len(s)):
                if s[r] not in x:
                    x += s[r]
                else:
                    break
            new.append(len(x))
        
        if len(new) == 0:
            return 0  

        return max(new)
        """
        :type s: str
        :rtype: int
        """
        