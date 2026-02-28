class Solution(object):
    def maximumValue(self, strs):
        x = []
        for i in strs:
            if i.isalpha():
                x.append(len(i))
            elif i.isdigit():
                x.append(int(i))
            else:
                x.append(len(i))
        return max(x)
        """
        :type strs: List[str]
        :rtype: int
        """
        