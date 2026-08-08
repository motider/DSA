class Solution(object):
    def firstUniqChar(self, s):
        count = {}

        for i in s:
            if i in count:
                count[i] +=1
            else:
                count[i] = 1

        for index, char in enumerate(s):
            if count[char] == 1:
                return index  
                
        return -1 
        """
        :type s: str
        :rtype: int
        """
        