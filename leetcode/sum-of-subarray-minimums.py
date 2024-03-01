class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        nextstack=[len(arr)]*len(arr)
        prevstack=[-1]*len(arr)
        stack=[]
        mod=(10**9+7)
        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            if stack:
                prevstack[i] = stack[-1]
            stack.append(i)
        stack=[]
        for j in range(len(arr)):
            while stack and arr[stack[-1]]>=arr[j]:
                a=stack.pop()
                nextstack[a]=j
            stack.append(j)
        ans=0
        print(prevstack)
        print(nextstack)
        for i in range(len(nextstack)):
            ans+=(((i-prevstack[i])*(nextstack[i]-i))*arr[i])%mod
        return ans%mod



        

        