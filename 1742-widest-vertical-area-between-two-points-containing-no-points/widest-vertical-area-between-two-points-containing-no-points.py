class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[0])
        print(points)
        z = []
        for i,j in points:
            z.append(i)
        print(z)
        arr = []
        for i in range(len(z)-1):       
            arr.append(z[i+1] - z[i])   
        return max(arr)

        