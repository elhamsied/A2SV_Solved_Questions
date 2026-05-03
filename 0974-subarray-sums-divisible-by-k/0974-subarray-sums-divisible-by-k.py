class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        prfx = 0
        ans = 0

        for i in nums:
            prfx += i
            rem = prfx % k

            ans += cnt[rem]
            cnt[rem] += 1
        return ans