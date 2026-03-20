class Solution(object):
    def flipAndInvertImage(self, image):
        n = len(image)
        
        for row in image:
            left, right = 0, n - 1
            
            while left <= right:
                # Flip + invert in one step
                row[left], row[right] = 1 - row[right], 1 - row[left]
                left += 1
                right -= 1
        
        return image
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        