class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ss="abcdefghijklmnopqrstuvwxyz"
        count=0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if ss.index(strs[j][i])>ss.index(strs[j+1][i]):
                    count+=1
                    break
        return count 
        
        