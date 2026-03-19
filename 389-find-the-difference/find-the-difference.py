class Solution(object):
    def findTheDifference(self, s, t):
        from collections import Counter


        x = Counter(s)
        y = Counter(t)

        new = y - x
        return list(new.elements())[0]
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        