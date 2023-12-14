class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.counter = defaultdict(int)

    def add(self, number: int) -> None:
        prev_freq = self.freq[number]
        self.freq[number] += 1
        self.counter[prev_freq] -= 1
        self.counter[self.freq[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.freq[number] > 0:
            prev_freq = self.freq[number]
            self.freq[number] -= 1
            self.counter[prev_freq] -= 1
            self.counter[self.freq[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.counter[frequency] > 0

      
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)