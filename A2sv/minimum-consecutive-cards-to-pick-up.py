class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        helper=defaultdict(int)
        j=0
        ans=float("inf")
        for i in range(len(cards)):
            helper[cards[i]]+=1
            while helper[cards[i]]!=1:
                helper[cards[j]]-=1
                ans=min(ans,i-j+1)
                j+=1
        if ans==float("inf"):
            return -1
        return ans

        