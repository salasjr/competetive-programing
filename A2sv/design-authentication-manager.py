class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.lst={}
        self.time=timeToLive
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.lst[tokenId]=currentTime + self.time

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.lst and currentTime <self.lst[tokenId]:
            self.lst[tokenId]=currentTime + self.time
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count=0
        for i in self.lst.values():
            if currentTime < i:
                count+=1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)