class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        man = sorted(nums, key=lambda x: str(x)*10, reverse=True)
        strs = ""
        for i in man:
            strs += str(i)
            s = str(i)   
            if len(s) > 1 and s[1] == '0':
                pass   
            elif len(s) == 1:
                pass   
            else:
                pass  
        if strs[0] == "0":
            strs = "0" 
        return strs

        
        