class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for key,value in freq.items():
            buckets[value].append(key)
        ans = []
        for i in range(len(buckets) -1,-1,-1):
            for element in buckets[i]:
                ans.append(element)
                if len(ans) == k:
                    return ans




        