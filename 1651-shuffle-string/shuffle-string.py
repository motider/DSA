class Solution(object):
    def restoreString(self, s, indices):
        x = list(s)
        new = list(zip(indices,x))

        fin = sorted(new, key = lambda x: x[0])

        ans = [i[1] for i in fin]

        answer = "".join(ans)
        return answer
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        