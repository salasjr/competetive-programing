class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        targetl,targetr=left,right
        flag=False
        for i in range(len(ranges)):
            a,b=ranges[i]
            if a<=targetl and b>=targetl:
                targetl=b+1
                flag=True
        if targetl-1>=targetr and flag:
            return True
        return False
                
            
        