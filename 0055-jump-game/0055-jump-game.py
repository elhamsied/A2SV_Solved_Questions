class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0:
            return True 
        steps = 0
        
        for i in range(n):
            if i > steps:
                return False
            steps = max(steps, i + nums[i])
            if steps >= n - 1:
                return True
        return False
