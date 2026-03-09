class Solution(object):
    def mostFrequentEven(self, nums):
        counts = list(map(lambda val: nums.count(val), nums))
        new = list(zip(nums, counts))

        evens = [u for u in new if u[0] % 2 == 0 ]

        if not evens:
            return -1
        else:
            max_count = max(u[1] for u in evens)
            candidates = [u[0] for u in evens if u[1] == max_count]

            result = min(candidates)
            return result
        """
        :type nums: List[int]
        :rtype: int
        """
        