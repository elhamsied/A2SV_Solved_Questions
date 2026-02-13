class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = Counter()
        for day_responses in responses:
            unique_today = set(day_responses)
            for resp in unique_today:
                count[resp] += 1
        max_freq = max(count.values())
        candidates = [resp for resp, freq in count.items() if freq == max_freq]
        return min(candidates)
