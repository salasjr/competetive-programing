class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i,needed,summ=0,0,0
        lenn=len(nums)
        while summ<n:
            if i<lenn and nums[i]<=summ+1:
                summ+=nums[i]
                i+=1
            else:
                needed+=1
                summ+=(summ+1)
        return needed



        