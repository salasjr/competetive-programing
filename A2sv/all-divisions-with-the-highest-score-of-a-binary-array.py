class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        dict_1={}
        dict_1[0]=0
        dict_2={}
        score=0
        for i in range(len(nums)):
            if nums[i]==0:
                score+=1
            dict_1[i+1]=score
        score=0
        dict_2[len(nums)]=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==1:
                score+=1
            dict_2[i]=score
        
        ans={}
        ans1=[]
        for i in range(len(nums)+1):
            z=dict_1[i]+dict_2[i]
            ans[i]=z
        sort_dict=sorted(ans.items(),key=lambda x:x[1],reverse=True)
        ans1=[sort_dict[0][0]]
        for i in range(1,len(sort_dict)):
            if sort_dict[i][1] !=sort_dict[0][1]:
                break
            else:
                ans1.append(sort_dict[i][0])
        return ans1
            
       
        
       

            
        