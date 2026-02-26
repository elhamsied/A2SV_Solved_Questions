class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win_sum = 0
        maximum = float('-inf')
        for i in range(k):
            win_sum += nums[i]
        maximum = win_sum
        lft = 0
        for rgt in range(k,len(nums)):
            win_sum += nums[rgt]
            win_sum -= nums[lft]
            maximum = max(win_sum, maximum)
            lft +=1
        return maximum /k