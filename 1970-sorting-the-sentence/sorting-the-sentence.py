class Solution:
    def sortSentence(self, s: str) -> str:
        x = s.split()
        print(x)
        arr = []
        for word in x:
            z = word[::-1]
            arr.append(z)
        print(arr)
        fif = sorted(arr)
        print(fif)
        oper = []
        for words in fif:
            yes = words[::-1]
            oper.append(yes)
        print(oper)
        strs = ""
        for i in oper:
            strs+=i
        print(strs)
        new_string = ""
        for char in strs:
            if char.isdigit():
                new_string += " "
            else:
                new_string += char
        final = new_string[:-1]
        return final


                