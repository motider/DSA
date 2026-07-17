class Solution(object):
    def minimumCardPickup(self, cards):
        l = 0
        maps = {}
        new = len(cards) + 1

        for r, num in enumerate(cards):
            if num in maps and maps[num] >= l:
                length = r - maps[num] + 1
                new = min(new, length)
                
                l = maps[num] + 1
                
            maps[num] = r
            
        if new > len(cards):
            return -1
        else:
            return new

        """
        :type cards: List[int]
        :rtype: int
        """
        