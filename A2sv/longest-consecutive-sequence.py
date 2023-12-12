class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        firstnum=float("inf")
        lastnum=float("inf")
        ans=0
        for i in nums:
            if (i<=firstnum or i>=lastnum) :
                firstnum=i
                while (i+1) in num:
                    i+=1
                lastnum=i
                while (firstnum-1) in  num:
                    firstnum-=1
            else:
                continue
            ans=max(ans,lastnum-firstnum+1)
        return ans
            
            
            
       