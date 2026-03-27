class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()

        new = []

        l = 0
        while l < len(arr)-1:
            y = arr[l],arr[l+1]
            new.append(list(y))
            l+=1

        fin = list(map(lambda a : a[1]-a[0] , new))
        final = min(fin)

        zipped_arr = list(zip(new,fin))

        final_answer = []
        for i in zipped_arr:
            if i[1] == final:
                final_answer.append(i[0])
                
        return final_answer
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        