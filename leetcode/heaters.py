class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        if houses==heaters:
            return 0
        if len(houses)==1 and houses[0] in heaters:
            return 0
        houses.sort()
        heaters.sort()
        def good(n):
            i, j = 0, 0  
            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) <=n:
                    i += 1
                else:
                    j += 1
            
            return i == len(houses)
        z=max(heaters)
        y=max(houses)
        low,high=1,max(z-min(houses),y-min(houses))
        ans=0
        while low <= high:
            mid=low+(high-low)//2
            if good(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans



        