class Solution(object):
    def addToArrayForm(self, num, k):
        x = ""
        for i in num:
            y = str(i)
            x+=y
            
        fin = int(x) + k
        ans = list(str(fin))
        answer = [int(r) for r in ans]
        return answer
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        