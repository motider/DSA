class Solution(object):
    def thousandSeparator(self, n):
        x = str(n)

        if len(x) < 4:
            return x
            
        if len(x) >= 4:
            y = list(x)
            for i in range(len(y) - 3, 0, -3):
                y.insert(i, ".")
            
            ans = "".join(y)
            return ans 

        """
        :type n: int
        :rtype: str
        """
        