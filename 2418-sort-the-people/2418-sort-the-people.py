class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dictionary = {k: v for k, v in zip(heights, names)}
        sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[0]))
        list1= list(sorted_dict.values())
        list1.reverse()
        return list1
       
            

            
        
        