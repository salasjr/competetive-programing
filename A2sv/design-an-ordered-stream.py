class OrderedStream:
    def __init__(self, n: int):
        self.lst = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.lst[idKey-1] = value
        ans = []
        while self.ptr < len(self.lst) and self.lst[self.ptr]:
            ans.append(self.lst[self.ptr])
            self.ptr += 1
        return ans
        
        

            
        
        
       
        

        
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)