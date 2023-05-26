from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        m=sorted(freq.items(),key=lambda x:-x[1])
        ans=''
        for i in range(len(m)):
            ans+=m[i][0]*m[i][1]
            
        return ans
        