class Solution(object):
    def minimumRecolors(self, blocks, k):
        w_count = blocks[:k].count('W')
        maxim = w_count

        for r in range(k, len(blocks)):
            if blocks[r] == 'W':     
                w_count += 1
            if blocks[r - k] == 'W': 
                w_count -= 1
                
            maxim = min(maxim, w_count)

        return maxim
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        