class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dupli = -1
        for i in nums:
            idx = abs(i) - 1
            if nums[idx] < 0:
                dupli = abs(i)
            else:
                nums[idx] = -nums[idx]
        
        missing = -1
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break
                
        return [dupli, missing]