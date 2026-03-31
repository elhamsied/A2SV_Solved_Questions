class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def get_starting_pos(nums, target):
            l, r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    ans = mid
                    r = mid - 1  
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return ans

        def get_ending_pos(nums, target):
            l, r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    ans = mid
                    l = mid + 1   
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return ans

        return [get_starting_pos(nums, target), get_ending_pos(nums, target)]
