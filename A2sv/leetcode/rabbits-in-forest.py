class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans=0
        mydict=Counter(answers)
        for key in mydict:
            if key==0:
                ans+=mydict[key]
            else:
                ans+=math.ceil(mydict[key]/(key+1))*(key+1)
        return ans
    

        