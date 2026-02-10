class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for index,value in enumerate(nums):
            x = target - value
            if x in num_map:
                return [num_map[x],index]
            num_map[value] = index
