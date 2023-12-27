class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        a = sorted(points, key=lambda x: x[0])
        ans=float("-inf")
        for i in range(len(a)-1):
            x=a[i][0]
            y=a[i+1][0]
            ans=max(ans,y-x)
        return ans
