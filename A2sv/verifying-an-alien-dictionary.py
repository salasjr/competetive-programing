class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={}
        for i in range(len(order)):
            d[order[i]]=i
        checker=[]
        for i in range(len(words)):
            a=words[i]
            x=[]
            for j in a:
                x.append(int(d[j]))
            checker.append(x)
        maxx=0
        for i in range(len(checker)):
            maxx=max(len(checker[i]),maxx)
        for j in range(len(checker)):
            a=len(checker[j])
            for i in range(a,maxx):
                checker[j].append(float("-inf"))
                
        left=0
        while left < (len(checker)-1):
            d=0
            while d<(len(checker[left])):
                if checker[left][d]<checker[left+1][d]:
                    break
                if checker[left][d]==checker[left+1][d]:
                    d+=1
                else:
                    return False   
            left+=1      
        return True

            

                
            
                    
                    
                    
                
                
                    
                
                

        
            
                
                
                    
                    
        
        
        
       
                
        
        
        