class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum1=sum(chalk)
        n=len(chalk)
        if k%sum1 == 0:
            return 0
        remain = k%sum1
        for i in range(n):
            remain-=chalk[i]
            if remain<0:
                return i
                
      
