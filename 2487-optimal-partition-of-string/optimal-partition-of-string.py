class Solution(object):
    def partitionString(self, s):
        l = 0
        maps = {}
        new = []

        for r, char in enumerate(s):
            if char in maps and maps[char] >= l:
                x = s[l:r]
                new.append(x)
                l = r 
                
            maps[char] = r

        if l < len(s):
            new.append(s[l:])
            
        return len(new)
        """
        :type s: str
        :rtype: int
        """
        