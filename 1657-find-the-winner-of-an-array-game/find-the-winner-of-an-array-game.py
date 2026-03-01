class Solution(object):
    def getWinner(self, arr, k):
        win_count = 0
        max_val = max(arr)

        while win_count < k:
            if arr[0] == max_val:
                break
                
            if arr[0] > arr[1]:
                win_count += 1
                loser = arr.pop(1)
                arr.append(loser)
            else:
                win_count = 1
                loser = arr.pop(0)
                arr.append(loser)

        return arr[0]
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        