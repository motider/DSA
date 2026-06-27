class Solution(object):
    def frequencySort(self, s):
        freq = {}
        for let in s:
            if let in freq:
                freq[let] +=1
            else:
                freq[let] = 1
            
        new = list(freq.items())
        x = sorted(new, key=lambda x:x[1], reverse = True)

        final = []
        for i in x:
            y = i[0]*i[1]
            final.append(y)
        ans = "".join(final)
        return ans
        """
        :type s: str
        :rtype: str
        """
        