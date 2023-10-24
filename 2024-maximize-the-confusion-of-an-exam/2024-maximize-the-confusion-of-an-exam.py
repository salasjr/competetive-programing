class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans=i=0
        d={"T":0,"F":0}
        for j in range(len(answerKey)):
            d[answerKey[j]]+=1
            ans=max(ans,d[answerKey[j]])
            if j-i+1>ans+k:
                d[answerKey[i]]-=1
                i+=1
        return len(answerKey)-i
            
       

            
        