class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = 0
        ans =[]
        for i in range(len(nums)):
            running+=nums[i]
            ans.append(running)
        return ans