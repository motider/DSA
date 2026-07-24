class Solution(object):
    def areOccurrencesEqual(self, s):
        freq = {}
        for i in s:
            if i in freq:
                freq[i] +=1
                
            if i not in freq:
                freq[i] = 1
                
                
        for i in freq.values():
            if i != freq[s[0]]:
                return False
                break
        else:
            return True
        """
        :type s: str
        :rtype: bool
        """
        