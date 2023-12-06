class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        tim=0
        for i in range(len(points)-1):
            a,b=points[i]
            c,d=points[i+1]
            tim1=abs(c-a)
            tim2=abs(b-d)
            tim+=max(tim1,tim2)
        return tim
                
            
        
        