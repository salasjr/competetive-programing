class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ss=[j for j in s]
        ans=[]
        for i in range(len(indices)):
            ans.append([ss[i],indices[i]])
        sorted_list = sorted(ans, key=lambda x: x[1])
        ans1=""
        for i in range(len(sorted_list)):
            a,b=sorted_list[i]
            ans1+=a
        return ans1
       