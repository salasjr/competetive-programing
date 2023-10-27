class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        ans = 0
        i = 0
        aliceWater = capacityA
        bobWater = capacityB
        j = len(plants) - 1

        while i < j:
            if plants[i] > aliceWater:
                ans += 1
                aliceWater = capacityA

            if plants[j] > bobWater:
                ans += 1
                bobWater = capacityB
            aliceWater -= plants[i]
            bobWater -= plants[j]
            i += 1
            j -= 1
            print(i,j)

        if plants[j] > bobWater and plants[i] > aliceWater and i == j:
            ans += 1
            AlicWater = capacityB

        return ans


       
        
        
        
        
        
    

        