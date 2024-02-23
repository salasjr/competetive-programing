class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr=[]
        for i in range(len(costs)):
            a,b=costs[i]
            arr.append([a-b,i])
        arr.sort() 
        ans=0
        for i in range(len(arr)):
            a,b=arr[i]
            if i<(len(costs)//2):
                ans+=costs[b][0]
            else:
                ans+=costs[b][1]
        return ans

        print(arr)

        