class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        curr_sum = sum(arr[:k])
        count = 0

        target_sum = threshold * k
        if curr_sum >= target_sum:
            count += 1

        for i in range(k, len(arr)):
            curr_sum += arr[i] - arr[i-k]
            
            if curr_sum >= target_sum:
                count += 1

        return count
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        