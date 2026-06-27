class Solution(object):
    def topKFrequent(self, words, k):
        freq = {}
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

        x = list(freq.items())

        new = sorted(x, key=lambda x: (-x[1], x[0]))

        final = []
        for i in range(k):
            final.append(new[i][0])
        return final
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        