class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<10:
            return []
        d = dict()
        for i in range(len(s)-9):
            key = s[i:i+10]
            if key not in d:
                d[key] = 1
            else:
                d[key] += 1
        return [key for key in d.keys() if d[key] > 1]
        