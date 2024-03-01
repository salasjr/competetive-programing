class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans=False
        m=len(board)
        n=len(board[0])
        dirr=[(0,1),(1,0),(0,-1),(-1,0)]
        def valid(i,j):
            return 0<=i<m and 0<=j<n
        def backtrack(r,c,path,seen):
            if "".join(path)==word:
                return True

            if path[-1] != word[len(path) - 1]:
                return False
            elif len(path)>len(word):
                return
            for i,j in dirr:
                x,y=r+i,c+j
                if valid(x,y) and (x,y) not in seen:
                    path.append(board[x][y])
                    seen.add((x,y))
                    if backtrack(x,y,path,seen):
                        return True
                    path.pop()
                    seen.remove((x,y))
        for i in range(m):
            for j in range(n):
                if backtrack(i,j,[board[i][j]],{(i,j)}):
                    return True
        return False

        
