class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mydict={0:1}
        summ=0
        ans=0
        for i in nums:
            summ+=i
            if (summ-goal) in mydict:
                ans+=(mydict[summ-goal])
            mydict[summ]=mydict.get(summ,0)+1
        return ans



        