class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        k=0
        z=0
        l=float('inf')
        nums.sort()
        if len(nums)%2 !=0:
            l=nums.pop(0)
        arr= sorted(nums)
        for i in range((len(nums)//2)-1,-1,-1):
            nums[k]=arr[i]
            nums[k+1]=arr[-(z+1)]
            k+=2
            z+=1
        if l!=float('inf'):
            nums.append(l)
        
            
        
        """
        Do not return anything, modify nums in-place instead.
        """
        