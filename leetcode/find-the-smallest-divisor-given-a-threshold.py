class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def divide(n):
            totalsum=0
            for i in nums:
                res=math.ceil(i/n)
                totalsum+=res
            return totalsum<=threshold
        
        low,high=1,max(nums)
        ans=0
        while low<=high:
            divisor=low+(high-low)//2

            if divide(divisor):
                ans=divisor
                high=divisor-1
            else:
                low=divisor+1
        return ans



        








        