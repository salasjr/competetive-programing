class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mydict={0:1}
        summ=0
        ans=0
        for i in nums:
            summ+=i
            if (summ-k) in mydict:
                ans+=(mydict[summ-k])
            mydict[summ]=mydict.get(summ,0)+1
        return ans


        