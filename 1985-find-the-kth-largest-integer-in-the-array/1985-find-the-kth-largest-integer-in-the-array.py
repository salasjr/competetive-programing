class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nm = [ int(i) for i in nums]
        nm.sort()
        ans = nm[len(nm)-k]
        return str(ans)
        

            
                
        