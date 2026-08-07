class Solution(object):
    def findTheDifference(self, s, t):
        x = list(s)
        y = list(t)
        x.sort()
        y.sort()
        x.append(0)

        ans = ""
        for i in range(len(x)):
            if x[i] != y[i]:
                ans+=y[i]
                break
            
        return ans

        """
        :type s: str
        :type t: str
        :rtype: str
        """
        