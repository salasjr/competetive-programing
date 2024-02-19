class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        needed=0
        totaldict={5:0,10:0,20:0}
        for i in bills:
            totaldict[i]+=1
            needed=i-5
            if needed==5:
                if  totaldict[5]==0:
                    return False
                else:
                    totaldict[5]-=1
            if needed==15:
                if totaldict[5]==0:
                    return False 
                elif (totaldict[10]==0) and totaldict[5]<3:
                    return False
                else:
                    if totaldict[10]:
                        totaldict[10]-=1
                        totaldict[5]-=1
                    else:
                        totaldict[5]-=3
        return True
           

        