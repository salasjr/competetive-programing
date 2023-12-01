class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        if len(word1)>len(word2):
            target=word1
        else:
            target=word2            
        x=min(len(word1),len(word2))
        for i in range(x):
            ans+=word1[i]
            ans+=word2[i]
        ans+=target[x:]
        return ans
        