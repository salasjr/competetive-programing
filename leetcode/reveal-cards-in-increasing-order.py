class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        
        q = deque(range(n))
        
        result = [0] * n
        for card in deck:
            result[q.popleft()] = card
            if q:
                q.append(q.popleft())
        
        return result
        