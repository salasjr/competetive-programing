class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans=[0]*(n+2)
        for i in bookings:
            a,b,c=i[0],i[1],i[2]
            ans[a]+=c
            ans[b+1]-=c
        for i in range(1,len(ans)):
            ans[i]=ans[i]+ans[i-1]
        return ans[1:n+1]        