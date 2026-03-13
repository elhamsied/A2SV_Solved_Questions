class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 0
        min_p = 0
        for i in range(len(nums)):
            startValue += nums[i]
            min_p = min(min_p,startValue)
        return 1- min_p
