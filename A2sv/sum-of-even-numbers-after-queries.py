class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum=0
        ans=[]
        for i in nums:
            if i%2==0:
                even_sum+=i
        for num,idx in queries:
            curr=nums[idx]
            if nums[idx]%2==0:
                even_sum-=nums[idx]
            nums[idx]+=num
            if nums[idx] %2==0:
                even_sum+=nums[idx]
            ans.append(even_sum)
        return ans
        
        
        