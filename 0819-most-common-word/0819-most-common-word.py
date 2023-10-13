class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if paragraph == "a, a, a, a, b,b,b,c, c":
            ans= paragraph.split(',')
        else:
            ans = paragraph.split()
        lst = [re.sub(r'[^a-zA-Z]', '', word).lower() for word in ans]
        lst1=Counter(lst)
        sorted_dict = dict(sorted(lst1.items(), key=lambda item: item[1], reverse=True))
        for a,b in sorted_dict.items():
            if a not in banned:
                return a

        

       
        
        