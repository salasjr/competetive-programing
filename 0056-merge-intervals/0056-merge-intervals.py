class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
        intervals.sort(key=lambda i:i[0])
        ans=[intervals[0]]
        for a,b in intervals[1:]:
            lastelement = b
            if a <= ans[-1][1]:
                ans[-1][1]=max(lastelement,ans[-1][1])
            else:
                ans.append([a,b])
        return ans
        
            
          

        