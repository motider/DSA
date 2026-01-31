class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        arr = []

        while l <= r:
            if height[l] < height[r]:
                arr.append(height[l]*(r-l))
                l += 1
            else:
                arr.append(height[r]*(l-r))
                r -= 1
        pos = list(map(abs, arr))
        return max(pos)
        """
        :type height: List[int]
        :rtype: int
        """
        