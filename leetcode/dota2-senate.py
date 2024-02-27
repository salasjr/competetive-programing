class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senators = list(senate)
        count_d, count_r = senate.count("D"), senate.count("R")
        ban_r = 0
        ban_d = 0

        while count_d > 0 and count_r > 0:
            print(senators)
            for i in range(len(senators)):
                if senators[i] == "R":
                    if ban_r:
                        ban_r -= 1
                        senators[i] = "X"  
                    else:
                        ban_d += 1
                        count_d -= 1
                elif senators[i] == "D":
                    if ban_d:
                        ban_d -= 1
                        senators[i] = "X"  
                    else:
                        ban_r += 1
                        count_r -= 1

        return "Radiant" if count_r > 0 else "Dire"
