class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        
        counter1 = Counter(t)
        counter2 = Counter()
        required_chars = len(counter1)
        formed_chars = 0
        l = 0
        r = 0
        min_len = float('inf')
        result = ""
        
        while r < len(s):
            char = s[r]
            counter2[char] += 1
            if char in counter1 and counter2[char] == counter1[char]:
                formed_chars += 1
            
            while formed_chars == required_chars and l <= r:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    result = s[l:r + 1]
                
                char = s[l]
                counter2[char] -= 1
                if char in counter1 and counter2[char] < counter1[char]:
                    formed_chars -= 1
                
                l += 1
            
            r += 1

        return result