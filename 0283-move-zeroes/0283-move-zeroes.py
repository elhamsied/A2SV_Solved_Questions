class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        seeker = 0
        for holder in range(len(nums)):
            if nums[holder] != 0:
                nums[seeker],nums[holder] = nums[holder],nums[seeker]
                seeker +=1
        """
        Do not return anything, modify nums in-place instead.
        """
        