class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        y = ""
        z = min(len(word1),len(word2))
        for i in range(z):
            y+=word1[i] + word2[i]
        else:
            if len(word1) > z:
                y+=word1[z:]
            elif len(word2) > z:
                y+=word2[z:]

        return y
        
        
        
  
        