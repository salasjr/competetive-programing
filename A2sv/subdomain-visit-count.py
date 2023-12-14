class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d={}
        answer=[]
        for i in cpdomains:
            lst=i.split()
            b=""
            z=lst[1]
            c=z.split(".")
            a = ""  
            for item in reversed(c):
                a = f"{item}.{a}" if a else item 
                d[a] = d.get(a, 0) + int(lst[0])
        for a,b in d.items():
            z=str(b) + " "+ a
            answer.append(z)
        return answer
            
            
      