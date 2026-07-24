class Solution(object):
    def mostWordsFound(self, sentences):
        new = []
        for i in sentences:
            x = i.split()
            new.append(len(x))
            
        return max(new)
        """
        :type sentences: List[str]
        :rtype: int
        """
        