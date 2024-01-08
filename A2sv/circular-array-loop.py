class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n=len(nums)
        visted=set()
        for i in range(n):
            if i not in visted:
                checked=set()
                while True:
                    if i in checked:
                        return True
                    visted.add(i)
                    checked.add(i)
                    prev,i=i,(i+nums[i])%n
                    if prev == i:
                        break
                    if nums[prev]>0 != nums[i]<0:
                        break
        return False 

            
            
        

        