class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pre=[0]*(10**5+1)
        n=float("-inf")
        for i in requests:
            a,b=i
            n=max(b,n)
            pre[a]+=1
            pre[b+1]-=1
        for i in range(1,len(pre)):
            pre[i]=pre[i-1]+pre[i]
        pre.sort()
        a=pre[::-1]
        nums.sort()
        nums=nums[::-1]
        ans=0
        for i in range(n+1):
            ans+=(nums[i]*a[i])
        return ans%((10**9)+7)

        