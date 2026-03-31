class Solution:
    def mySqrt(self, x: int) -> int:
        right = x
        left = 0
        ans = -1
        while left <= right:
            mid = (left + right)//2
            res = mid*mid
            if res == x:
                return mid
            elif (res> x):
                right = mid -1
            else:
                ans = mid 
                left = mid +1
        return ans