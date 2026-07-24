class Solution(object):
    def countPrefixes(self, words, s):
        new = 0
        for i in words:
            x = len(i)
            if i == s[:x]:
                new+=1
                
        return new
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        