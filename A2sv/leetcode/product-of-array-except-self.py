class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forr=[]
        back=[]
        ans=[]
        pro=1
        for i in range(len(nums)):
            forr.append(pro)
            pro*=nums[i]
        pro=1
        for j in range(len(nums)-1,-1,-1):
            back.append(pro)
            pro*=nums[j]
        back=back[::-1]
        for i in range(len(back)):
            ans.append(forr[i]*back[i])
        return ans
            