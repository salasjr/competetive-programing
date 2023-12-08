class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losser=[]
        winner=[]
        ans1=[]
        for i in range(len(matches)):
            a,b=matches[i]
            winner.append(a)
            losser.append(b)
        winner_dict=Counter(winner)
        losser_dict=Counter(losser)
        for a  in winner_dict.keys():
            if a in losser_dict:
                continue
            else:
                ans1.append(a)
        ans2=[]
        for a,b in losser_dict.items():
            if b==1:
                ans2.append(a)
        ans1.sort()
        ans2.sort()
        return [ans1,ans2]
        
        