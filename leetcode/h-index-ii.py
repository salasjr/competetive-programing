class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def good(n):
            count=0
            for i in citations:
                if i>=n:
                    count+=1
            return count>=n

        low,high=0,len(citations)
        res=0
        while low<=high:
            mid=low+(high-low)//2
            if good(mid):
                res=mid
                low=mid+1
            else:
                high=mid-1
        return res



        