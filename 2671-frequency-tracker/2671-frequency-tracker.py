class FrequencyTracker:

    def __init__(self):
        self.nums = defaultdict(int)
        self.Counts = defaultdict(int)

    def add(self, number: int) -> None:
        self.nums[number] += 1
        nums_freq = self.nums[number]
        if nums_freq > 1:
            self.Counts[nums_freq] += 1
            self.Counts[nums_freq - 1] -= 1
        else:
            self.Counts[nums_freq] += 1
 
    def deleteOne(self, number: int) -> None:
        if self.nums[number] > 0:
            self.nums[number] -= 1
            nums_freq = self.nums[number]
            self.Counts[nums_freq + 1] -= 1
            if nums_freq > 0:
                self.Counts[nums_freq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        if self.Counts[frequency] > 0:
            return True
        return False