class Solution(object):
    def freqAlphabets(self, s):
        alphabet_map = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', 
    '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10#': 'j', 
    '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', 
    '16#': 'p', '17#': 'q', '18#': 'r', '19#': 's', '20#': 't', 
    '21#': 'u', '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', 
    '26#': 'z'
}

        new = list(s)
        x = ""
        new.reverse()
        l = 0
        final = []
        while l < len(new):
            if new[l] == '#':
                y = new[l:l+3]
                z = "".join(y)
                final.append(alphabet_map[z[::-1]])
                l+=3
            else:
                final.append(alphabet_map[new[l]])
                l+=1
        ans = "".join(final)
        return ans[::-1]
        """
        :type s: str
        :rtype: str
        """
        