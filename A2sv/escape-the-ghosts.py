class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        minn=float("inf")
        minn2=abs(target[0])+abs(target[1])
        for i in range(len(ghosts)):
            a,b=ghosts[i]
            a=abs(a-target[0])+abs(b-target[1])
            minn=min(minn,a)
        print(minn,minn2)
        if minn2<minn:
            return True
        return False
            
        