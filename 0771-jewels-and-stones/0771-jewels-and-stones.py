class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s1=Counter(jewels)
        s2=Counter(stones)
        count=0
        for a,b in s2.items():
            if a in s1:
                count+=b
        return count