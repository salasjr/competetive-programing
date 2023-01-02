class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nm = [ int(i) for i in nums]
        nm.sort()
        ans = nm[len(nm)-k]
        return str(ans)
        
        
        # sorted(nums)
        # m = len(nums)
        # if m==k:
        #     return nums[0]
        # elif m== k+1:
        #     return nums[1]
        # else:
        #     return nums[m-k]
            
            
                
        