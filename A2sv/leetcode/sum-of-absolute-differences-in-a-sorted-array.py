class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre=[]
        summ=0
        for i in nums:
            pre.append(i+summ)
            summ+=i
        ans=[]
        for i in range(len(nums)):
            b=pre[-1]-pre[i]-(nums[i]*(len(nums)-i-1))
            ans.append(b)
        ans1=[]
        for i in range(len(nums)):
            b=((i+1)*nums[i])-pre[i]
            ans1.append(b)
        for i in range(len(ans)):
            ans[i]+=ans1[i]
        return (ans)


        
    