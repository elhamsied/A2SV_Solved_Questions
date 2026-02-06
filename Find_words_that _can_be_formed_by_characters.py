class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ava = Counter(chars)
        ans = 0
        for word in words:
            need = Counter(word)
            if all(need[i] <= ava[i] for i in need):
                ans += len(word)
        return ans
