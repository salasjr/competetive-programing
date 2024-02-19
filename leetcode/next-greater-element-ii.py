class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=nums+nums
        mydict={}
        stack=[0]
        for i in range(1,len(ans)):
            while stack and ans[i]>ans[stack[-1]]:
                j=stack.pop()
                mydict[j]=i
            stack.append(i)
        if len(nums) in mydict:
            z=ans[mydict[len(nums)]]
        else:
            z=-1
        ans1=[z]
        for i in range(1,len(nums)):
            if i in mydict:
                ans1.append(ans[mydict[i]])
            else:
                ans1.append(-1)
        return (ans1)


        