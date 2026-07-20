class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        new = 0
        for i in stones:
            if i in jewels:
                new+=1
        return new
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        