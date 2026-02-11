class Solution(object):
    def reverseVowels(self, s):
        x = list(s)
        l = 0
        r = len(s)-1
        while l<r:
            if s[l] in "aeiouAEIOU" and s[r] not in "aeiouAEIOU":
                r-=1
            elif s[l] not in "aeiouAEIOU" and s[r] in "aeiouAEIOU":
                l+=1
            elif s[l] in "aeiouAEIOU" and s[r] in "aeiouAEIOU":
                x[l],x[r] = x[r],x[l]
                l+=1
                r-=1
            else:
                l+=1
                r-=1
        y = "".join(x)
        return y
        """
        :type s: str
        :rtype: str
        """
        