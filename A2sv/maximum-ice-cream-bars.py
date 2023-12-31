class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxx=max(costs)
        lst=[0]*(maxx+1)
        for i in costs:
            lst[i]+=1
        sorted_array = []
        for i in range(len(lst)):
            sorted_array.extend([i] * lst[i])
        count=0
        ans=0
        for i in range(len(sorted_array)):
            if ans>=coins:
                return count
            elif ans + sorted_array[i]>coins:
                return count
            else:
                ans+=sorted_array[i]
                count+=1  
        return count
        
        