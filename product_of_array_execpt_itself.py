class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix = [1]
        prefix =[1]
        output = []
        for i in range(len(nums)-1):
            prefix.append(prefix[-1]*nums[i])
        print(prefix)
        for i in range(len(nums)-1, 0 ,-1):
            postfix.append(postfix[-1]*nums[i])
        print(postfix)
        for i in range(len(nums)):
            output.append(prefix[i]*postfix[-1-i])
        return output
     
