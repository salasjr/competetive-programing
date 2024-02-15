class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        ans=1
        last=points[0][1]
        first=points[0][0]
        print(points)
        for i in range(1,len(points)):
            a,b=points[i]
            if a>last:
                ans+=1
                last=b
            else:
                last=min(last,b)     
        return (ans)
        