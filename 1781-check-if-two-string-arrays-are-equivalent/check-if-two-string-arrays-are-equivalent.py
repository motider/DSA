class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        x = "".join(word1)
        y = "".join(word2)

        return x == y
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        