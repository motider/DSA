class Solution(object):
    def distributeCandies(self, candyType):
        n = len(candyType)

        x = n/2
        y = set(candyType)

        if len(y) >= x:
            return x
            
        if len(y) < x:
            return len(y)
        """
        :type candyType: List[int]
        :rtype: int
        """
        