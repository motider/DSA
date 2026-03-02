class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        from collections import Counter


        counts = Counter(s1.split() + s2.split())

        result = [word for word, count in counts.items() if count == 1]

        return result
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        