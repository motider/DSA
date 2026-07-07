class Solution(object):
    def isIsomorphic(self, s, t):
        dic = {}
        taken = set() 

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in taken:
                    return False
                    break
                dic[s[i]] = t[i]
                taken.add(t[i])
                
            if s[i] in dic and t[i] != dic[s[i]]:
                return False
                break
        else:
            return True
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        