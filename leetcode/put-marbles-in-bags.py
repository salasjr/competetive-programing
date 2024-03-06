class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights)==k:
            return 0
        maxsum=weights[0]+weights[-1]
        minsum=weights[0]+weights[-1]
        ans=[]
        for i in range(len(weights)-1):
            ans.append(weights[i]+weights[i+1])
        ans.sort()
        for i in range(k-1):
            minsum+=ans[i]
            maxsum+=ans[len(ans)-1-i]
        return (maxsum-minsum)


