class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans=[]
        lenn=max(len(list1),len(list2))
        word_with_index=[]
        for i in range(len(list1)):
            if list1[i] in list2:
                z=list2.index(list1[i])
                word_with_index.append([list1[i],z+i])
        word_with_index.sort(key=lambda x: x[1])
        i=0
        checker=word_with_index[0][1]
        for i in range (len(word_with_index)):
            if  word_with_index[i][1]==checker:
                ans.append(word_with_index[i][0])
       
        return ans
            
        