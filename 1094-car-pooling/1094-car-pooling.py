class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        events = []
        for passengers, start, end in trips:
            events.append((start, passengers))
            events.append((end, -passengers))

        events.sort()

        current_passengers = 0
        for location, passengers in events:
            current_passengers += passengers
            if not(0<=current_passengers <=capacity):
                return False

        return True







            
            

        
            
        
        
        