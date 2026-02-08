class FrequencyTracker:

    def __init__(self):
        self.freq = {}
        self.f = {}

    def add(self, number: int) -> None:
        if number in self.freq:
            self.freq[number] += 1
            self.f[self.freq[number]-1] -= 1
        else:
            self.freq[number] = 1

        
        if self.freq[number] in self.f:
            self.f[self.freq[number]] += 1
            
        else:
            self.f[self.freq[number]] = 1

    def deleteOne(self, number: int) -> None:
        if number in self.freq:
            if self.freq[number] == 1:
                self.f[1] -= 1
                del self.freq[number]
            else:
                self.f[self.freq[number]] -= 1
                self.freq[number] -= 1
                if self.freq[number] in self.f:
                    self.f[self.freq[number]] += 1
                else:
                    self.f[self.freq[number]] = 1

    def hasFrequency(self, frequency: int) -> bool:

        if frequency in self.f and self.f[frequency] > 0:
            return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)