class Solution(object):
    def isHappy(self, n):
        seen = set()  

        while True:
            x = str(n)
            y = list(x)
            
            fin = [int(i)**2 for i in y]
            final = sum(fin)
            
            if final == 1:
                return True
                break
            
            if final in seen:
                return False
                break
            
            seen.add(final)
            n = final
        """
        :type n: int
        :rtype: bool
        """
        