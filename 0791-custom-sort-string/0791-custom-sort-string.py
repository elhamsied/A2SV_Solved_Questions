class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        result = []

        for ch in order:
            if ch in count:
                result.append(ch * count[ch])
                del count[ch]

        for ch in count:
            result.append(ch * count[ch])

        return "".join(result)