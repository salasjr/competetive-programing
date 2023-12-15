class UndergroundSystem:

    def __init__(self):
        self.lst={}
        self.lst1={}
        self.lst2={}
        self.travel=defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.lst[id]=stationName
        self.lst1[id]=t
        self.travel[id].append(stationName)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.lst2[id]=t
        checkin=self.lst1[id]
        name=self.lst[id]
        diff=t-checkin
        self.travel[(name,stationName)].append(diff)        
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        b=self.travel[(startStation,endStation)]
        return sum(b)/len(b)
        
        
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)