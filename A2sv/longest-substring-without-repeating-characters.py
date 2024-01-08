class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        dict_={s[0]:1}
        l,r=0,1
        ans=0
        while r<len(s):
            if s[r] in dict_:
                ans=max(ans,len(dict_))
                dict_[s[l]]-=1
                if dict_[s[l]]==0:
                    dict_.pop(s[l])
                l+=1 
                
            else:
                dict_[s[r]]=1
                r+=1
        ans=max(ans,len(dict_))
        return ans
                
                


        