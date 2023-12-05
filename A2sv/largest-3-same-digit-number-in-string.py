class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i,l=0,3
        ans=[]
        while l<=len(num):
            if num[i]==num[i+1]==num[i+2]:
                ans.append(int(num[i:l]))
            i+=1
            l+=1
        ans.sort()
        if ans:
            if ans[-1]==0:
                return "000"
            return str(ans[-1])
        return ""
            
        