class Solution:
    def romanToInt(self, s: str) -> int:
        
        dicts = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        lis = []
        for index, char in enumerate(s):
            if index == len(s) - 1:  
                lis.append(dicts[char])
            else:
                char2 = s[index + 1]  
                if dicts[char] < dicts[char2]:
                    lis.append(-dicts[char])
                else:
                    lis.append(dicts[char])

        return sum(lis)

            
        


        
        