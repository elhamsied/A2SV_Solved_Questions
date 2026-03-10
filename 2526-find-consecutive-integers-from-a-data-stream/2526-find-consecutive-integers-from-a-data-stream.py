class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.q =deque()

    def consec(self, num: int) -> bool:
        self.q.append(num)
        if len(self.q)>self.k:
            self.q.popleft()
        if len(self.q)<self.k:
            return False
        for x in self.q:
            if x != self.value:
                return False
        return True
    

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
