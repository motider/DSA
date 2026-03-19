class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        from collections import Counter

        x = Counter(ransomNote)
        y = Counter(magazine)
        for k in x:
            if x[k] > y[k]:
                return False
                break   
        else:    
            return True


        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        