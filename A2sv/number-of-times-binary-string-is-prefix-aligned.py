class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count=0
        maxx=float("-inf")
        for i in range(len(flips)):
            maxx=max(maxx,flips[i])
            if maxx==i+1:
                count+=1
        return count
            
            
        