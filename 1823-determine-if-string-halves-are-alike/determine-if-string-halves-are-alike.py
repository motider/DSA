class Solution(object):
    def halvesAreAlike(self, s):
        x = s[:(len(s)//2)]
        y = s[(len(s)//2):]

        n = 0
        for i in x:
            if i in "aeiouAEIOU":
                n+=1
            
        m = 0
        for j in y:
            if j in "aeiouAEIOU":
                m+=1
            
            
        if m == n:
            return True
            
        else:
            return False
        """
        :type s: str
        :rtype: bool
        """
        