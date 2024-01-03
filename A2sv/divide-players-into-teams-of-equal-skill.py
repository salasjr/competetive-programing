class Solution(object):
    def dividePlayers(self, skill):
        x=len(skill)
        skill.sort()
        m = skill[0]+skill[x-1]
        count=0
        for i in range(x//2):
            z = skill[i] + skill[x-i-1]
            if z==m:
                n=skill[i]*skill[x-i-1]
                count+=n 
                
            else:
                return -1
        return count
            
            
        
        
        
        
           
            
            
    
    