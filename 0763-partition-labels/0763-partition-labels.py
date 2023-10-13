class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charlastpostion={}
        for a,c in enumerate(s):
            charlastpostion[c]=a
        ans=[]
        size, end =0,0
        for a,b in enumerate(s):
            size+=1
            end = max(end,charlastpostion[b])
            if a==end:
                ans.append(size)
                size = 0
        return ans