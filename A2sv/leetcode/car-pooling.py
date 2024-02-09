class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr=[0]*(10001)
        maxlen=float("-inf")
        for i in range(len(trips)):
            a,b,c=trips[i]
            arr[b]+=a
            arr[c]-=a
        summ=0
        for i in range(1001):
            summ=arr[i]+summ
            if summ>capacity:
                return False
        return True

       

        






            
            

        
            
        
        
        