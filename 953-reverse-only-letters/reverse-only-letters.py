class Solution(object):
    def reverseOnlyLetters(self, s):
        s_list = list(s)
        l = 0
        r = len(s_list) - 1  
        while l < r:
            if s_list[l].isalpha() and s_list[r].isalpha():
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1 
                r -= 1  
                    
            elif s_list[l].isalpha() and not s_list[r].isalpha():
                r -= 1
                
            elif not s_list[l].isalpha() and s_list[r].isalpha():
                l += 1
                
            else:
                l += 1
                r -= 1
                
        return "".join(s_list)
        """
        :type s: str
        :rtype: str
        """
        