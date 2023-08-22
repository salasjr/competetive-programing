class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x = edges[0][1]
        y = edges[0][0]
        if x in edges[1]:
            return x
        else:
            return y
        return edges[0][1]
#         adjst_list = collections.defaultdict(list) 
#         for x, y in edges:
#             adjst_list[x].append(y)
#             adjst_list[y].append(x)
#         for i in range(len(edges)-1):
        
            
       
        
        
        