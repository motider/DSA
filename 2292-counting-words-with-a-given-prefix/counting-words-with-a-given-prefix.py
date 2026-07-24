class Solution(object):
    def prefixCount(self, words, pref):
        n = len(pref)
        new = []
        for i in words:
            if i[:n] == pref:
                new.append(i)
                
        return len(new)
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        