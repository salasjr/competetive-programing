class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def good(cap):
            count=0
            total=0
            for i in nums:
                total+=i
                if total>cap:
                    count+=1
                    total=i
            return count+1<=k
        low,high=max(nums),sum(nums)
        res=sum(nums)
        while low<=high:
            mid=low +(high-low)//2
            if good(mid):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res


        