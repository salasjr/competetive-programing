class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        a=[a for a in range(1,20001)]
        count=0
        for i in a:
            if i not in arr:
                count+=1
            if count==k:
                return i
        
        
        