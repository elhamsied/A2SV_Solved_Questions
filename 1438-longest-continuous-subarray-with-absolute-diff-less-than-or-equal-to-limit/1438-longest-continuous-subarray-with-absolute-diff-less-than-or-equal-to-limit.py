class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = deque()
        max_queue = deque() 

        left = 0
        result = 0

        for right in range(len(nums)):
            # maintain min queue (increasing)
            while min_queue and min_queue[-1] > nums[right]:
                min_queue.pop()
            min_queue.append(nums[right])

            # maintain max queue (decreasing)
            while max_queue and max_queue[-1] < nums[right]:
                max_queue.pop()
            max_queue.append(nums[right])

            # shrink window if condition breaks
            while max_queue[0] - min_queue[0] > limit:
                if nums[left] == max_queue[0]:
                    max_queue.popleft()
                if nums[left] == min_queue[0]:
                    min_queue.popleft()
                left += 1

            result = max(result, right - left + 1)

        return result