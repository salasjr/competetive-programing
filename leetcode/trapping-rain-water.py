class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l,r=0,len(height)-1
        lvalue,rvalue=height[l],height[r]
        res=0
        while l<=r:
            if lvalue<rvalue:
                lvalue=max(lvalue,height[l])
                res+=(lvalue-height[l])
                l+=1
            else:
                rvalue=max(rvalue,height[r])
                res+=(rvalue-height[r])
                r-=1
        return res

                

        