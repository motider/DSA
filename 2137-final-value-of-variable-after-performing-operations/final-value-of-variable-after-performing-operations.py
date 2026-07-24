class Solution(object):
    def finalValueAfterOperations(self, operations):
        fin = 0

        for i in operations:
            if i == "--X" or i == "X--":
                fin-=1
                
            else:
                fin+=1
                
        return fin
        """
        :type operations: List[str]
        :rtype: int
        """
        