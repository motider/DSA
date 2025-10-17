class Solution(object):
    def reverseWords(self, s):
        x = ""
        words = s.split()
        words.reverse()
        jon = ','.join(words)
        new = jon.replace(",", " ")
        return new

        """
        :type s: str
        :rtype: str
        """
        