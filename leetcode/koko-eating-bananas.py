class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def good(curr):
            total=0
            for i in piles:
                z=math.ceil(i/curr)
                total+=z
                if total > h:
                    return False
            return True
        low,high=1,max(piles)
        ans=0
        while low <= high:
            mid=low+(high-low)//2
            if good(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans



        