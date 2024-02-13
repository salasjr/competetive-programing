class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d=defaultdict(list)
        for a,b in enumerate(nums):
            d[b].append(a)
        d2=defaultdict(list)
        for a in d:
            z=(d[a])
            run=[0]
            summ=0
            for i in z:
                summ+=i
                run.append(summ)
            d2[a]=run
        ans1=[0]*len(nums)
        ans2=[0]*len(nums)
        for  key in d2:
            value=d2[key]
            for i in range(1,len(value)):
                pree=d[key][i-1]*(i-1)-d2[key][i-1]+d2[key][-1]
                suff=-d2[key][i]-(d[key][i-1])*(len(d[key])-i)
                ans=pree+suff
                ans1[d[key][i-1]]=ans
        return ans1
        