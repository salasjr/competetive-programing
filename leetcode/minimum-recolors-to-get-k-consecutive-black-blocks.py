class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l,r=0,k-1
        ans=float("inf")
        while r<len(blocks):
            d=Counter(blocks[l:r+1])
            ans=min(d["W"],ans)
            l+=1
            r+=1
        return ans
        
        
        