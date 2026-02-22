class Solution(object):
    def sortVowels(self, s):
        l = 0
        y = []
        while l < len(s):
            if s[l] in "aeiouAEIOU":
                y.append(s[l])
            l += 1
        y.sort() 

        z = list(s)
        r = 0
        v = 0  
        while r < len(z): 
            if z[r] not in "aeiouAEIOU":
                r += 1
            else:
                z[r] = y[v] 
                v += 1      
                r += 1

        return "".join(z)

        """
        :type s: str
        :rtype: str
        """
        