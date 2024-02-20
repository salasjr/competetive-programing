class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row,col=len(matrix),len(matrix[0])
        pre=[[0]*col for _ in range(row)]
        for r in range(row):
            for c in range(col):
                top=pre[r-1][c] if r>0 else 0
                left=pre[r][c-1] if c>0 else 0
                topleft = pre[r-1][c-1] if min(r,c)>0 else 0
                pre[r][c]=matrix[r][c] + top + left - topleft
        ans=0
        for r1 in range(row):
            for r2 in range(r1,row):
                count=defaultdict(int)
                count[0]=1
                for c in range(col):
                    cur_sum=pre[r2][c]-(
                        pre[r1-1][c] if r1>0 else 0
                    )
                    diff=cur_sum-target
                    ans+=count[diff]
                    count[cur_sum]+=1
        print(count)
        return ans
        