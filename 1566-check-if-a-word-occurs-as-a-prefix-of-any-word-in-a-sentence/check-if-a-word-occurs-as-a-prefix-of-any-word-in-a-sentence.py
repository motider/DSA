class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        n = len(searchWord)
        fin = sentence.split()

        new = []
        for i in fin:
            if i[:n] == searchWord:
                new.append(fin.index(i) + 1)
                

        if len(new) == 0:
            return -1
            
        else:
            return min(new)
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        