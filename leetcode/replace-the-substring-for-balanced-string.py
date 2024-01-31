class Solution:
    def balancedString(self, s: str) -> int:
        def is_balanced(map, target):
            for value in map.values():
                if value > target:
                    return False
            return True
        map = {}
        target = len(s) // 4
        min_len = len(s)

        for c in s:
            map[c] = map.get(c, 0) + 1

        if is_balanced(map, target):
            return 0

        left = 0
        for right in range(len(s)):
            map[s[right]] -= 1
            if is_balanced(map, target):
                min_len = min(min_len, right - left + 1)
                while left <= right:
                    map[s[left]] += 1
                    left += 1
                    if is_balanced(map, target):
                        min_len = min(min_len, right - left + 1)
                    else:
                        break

        return min_len
        



       
        
        
        
        