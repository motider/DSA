class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        new = []

        for word in words:
            dic = {}
            taken = set()
            is_match = True 

            if len(word) != len(pattern):
                is_match = False
            else:
                for i in range(len(word)):
                    if word[i] not in dic:
                        if pattern[i] in taken:
                            is_match = False
                            break
                        
                        dic[word[i]] = pattern[i]
                        taken.add(pattern[i])
                    
                    if dic[word[i]] != pattern[i]:
                        is_match = False
                        break
            
            if is_match:
                new.append(word)
                
        return new
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        