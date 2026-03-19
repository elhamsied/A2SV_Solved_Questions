class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0

        for x, c in count.items():
            group = x + 1
            total += ((c + group - 1) // group) * group

        return total