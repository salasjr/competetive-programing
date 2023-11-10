class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda  x:x[0])
        prevend=intervals[0][1]
        count=0
        for a,b in intervals[1:]:
            if a>=prevend:
                prevend=b
            else:
                count+=1
                prevend=min(b,prevend)
        return count
   
        