class Solution(object):
    def customSortString(self, order, s):
        arr = ""

        for i in order:
            if i in s:
                arr+=i*s.count(i)
                
        new = []
        for n in s:
            new.append(n)
            
        new.sort()
        fin = "".join(new)

        for j in sorted(set(fin)):
            if j not in order:
                arr+=j*fin.count(j)
                
        return arr
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        