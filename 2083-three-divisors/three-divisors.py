class Solution(object):
    def isThree(self, n):
        new = []
        for i in range(1,n+1):
            if n % i ==0:
                new.append(i)
                
        if len(new) == 3:
            return True
        else:
            return False
        """
        :type n: int
        :rtype: bool
        """
        