class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
            
        target = sorted(s1)
        window_len = len(s1)
        
        for i in range(len(s2) - window_len + 1):
            substring = s2[i : i + window_len]
            
            if sorted(substring) == target:
                return True
                
        return False
        
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        