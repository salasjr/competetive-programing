class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums="1234567890"
        for i in range(len(word)):
            if word[i] not in nums:
                word= word.replace(word[i],' ')
        num_list=word.split()

        res=[]
        for i in range(len(num_list)):
            res.append(int(num_list[i]))

        return len(set(res))   
                
                
        