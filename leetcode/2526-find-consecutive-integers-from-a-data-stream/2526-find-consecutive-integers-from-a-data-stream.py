class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = 0
        self.value = value
        self.k = k        

    def consec(self, num: int) -> bool:
        
        if num != self.value:
            self.stream = 0
        else:
            self.stream += 1
        
        if self.stream >= self.k:
            return True
        return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)