class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        checker=defaultdict(int)
        summ=0
        ans=0
        j=0
        dict_={}
        for i in range(len(nums)):
            summ+=nums[i]
            checker[nums[i]]+=1
            while checker[nums[i]]>1:
                checker[nums[j]]-=1
                summ-=nums[j]
                j+=1
            ans=max(summ,ans)
        return ans
                

        