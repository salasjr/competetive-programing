class Solution:
    def printVertically(self, s: str) -> List[str]:
        lst=s.split()
        lenn=0
        for i in lst:
            lenn=max(lenn,len(i))
        lst1=[]
        for i in range(len(lst)):
            a=lst[i]
            b=[]
            for j in range(len(a)):
                b.append(lst[i][j])
            while len(b)<lenn:
                b.append("1")
            lst1.append(b)
        i=0
        anss=[]
        for i in range(lenn):
            ans1=""
            for j in range(len(lst1)):
                ans1+=lst1[j][i]
            anss.append(ans1)
        for i in range(len(anss)):
            for j in range(len(anss[i])):
                if anss[i][j] == '1':
                    anss[i] = anss[i][:j] + ' ' + anss[i][j+1:]
        anss = [s.rstrip() for s in anss]
        return anss
                
                
                
        