class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        a=capacity
        count=0
        ans=0
        for i in range(len(plants)):
            if plants[i]>capacity:
                ans+=2*count+1
                capacity=a
            else:
                ans+=1
            count+=1
            capacity-=plants[i]
        return ans
                
        