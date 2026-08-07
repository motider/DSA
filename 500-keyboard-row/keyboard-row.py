class Solution(object):
    def findWords(self, words):
        x = set("qwertyuiop")
        y = set("asdfghjkl")
        z = set("zxcvbnm")

        ans = []

        for i in words:
            word_set = set(i.lower())
            
            if word_set <= x or word_set <= y or word_set <= z:
                ans.append(i)

        return ans
        """
        :type words: List[str]
        :rtype: List[str]
        """
        