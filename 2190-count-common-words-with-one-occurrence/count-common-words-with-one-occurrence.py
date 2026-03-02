class Solution(object):
    def countWords(self, words1, words2):
        from collections import Counter

        count1 = Counter(words1)
        count2 = Counter(words2)

        final = 0
        for word, count in count1.items():
            if word in count2 and count == count2[word] == 1:
                final += 1

        return final
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        