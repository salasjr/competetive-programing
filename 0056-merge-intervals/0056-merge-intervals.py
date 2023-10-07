class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda  i:i[0] )
        ans=[intervals[0]]
        for a,b in intervals[1:]:
            last = ans[-1][1]
            if last >= a:
                ans[-1][1] = max(last,b)
            else:
                ans.append([a,b])
        return ans
            
          

        