class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        r=len(mat)
        c=len(mat[0])
        ans=[]
        cur_r=0
        cur_c=0
        up = True
        while len(ans) !=r*c:
            if up:
                while cur_r >=0 and cur_c< c:
                    ans.append(mat[cur_r][cur_c])
                    cur_r-=1
                    cur_c+=1
                if cur_c ==c:
                    cur_c-=1
                    cur_r+=2
                else:
                    cur_r+=1
                up =False
            else:
                while cur_c>=0 and cur_r< r:
                    ans.append(mat[cur_r][cur_c])
                    cur_r+=1
                    cur_c-=1
                if cur_r ==r:
                    cur_c+=2
                    cur_r-=1
                else:
                    cur_c+=1
                up =True
        return ans
            
       
        