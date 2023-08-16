class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incom = [0 for _ in range(n)] 
        out = [0 for _ in range(n)]
        for edge in trust:
            p1,p2 = edge
            out [p1-1]+=1
            incom [p2-1]+=1
        town_judge=-1
        for person in range(n):
            if incom[person]== n-1 and out[person]==0:
                town_judge=person+1
                break
        return town_judge
    
            
        