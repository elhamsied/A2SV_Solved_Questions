class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = Counter(nums)
        for i,freq in count.items():
            if freq == 1:
                return i
     
