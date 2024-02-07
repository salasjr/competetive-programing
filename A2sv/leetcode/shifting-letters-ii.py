class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        arr=list(map(ord,list(s)))
        checker=[0]*(n+1)
        for i in shifts:
            l,r=i[0],i[1]
            forward=i[2]
            if forward:
                checker[l]+=1
                checker[r+1]-=1
            else:
                checker[l]+=-1
                checker[r+1]-=-1
        for i in range(1,len(checker)):
            checker[i]=checker[i]+checker[i-1]
        ans=[]
        for a,b in enumerate(arr):
            z=chr(((b+checker[a]-97)%26)+97)
            ans.append(z)
        return "".join(ans)
        


        
        