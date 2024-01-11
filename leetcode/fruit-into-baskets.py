class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mydict=defaultdict(int)
        count=0
        ans=0
        j=0
        for i in range(len(fruits)):
            if fruits[i] not in mydict:
                count+=1
            while count>2:
                mydict[fruits[j]]-=1
                if mydict[fruits[j]]==0:
                    count-=1
                    del mydict[fruits[j]]
                j+=1
            print(j,i)
            mydict[fruits[i]]+=1
            ans=max(ans,i-j+1)
        return ans
            
    

        