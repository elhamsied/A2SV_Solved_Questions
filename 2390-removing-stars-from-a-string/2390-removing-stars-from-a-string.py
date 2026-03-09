class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for i in s:
            if i != '*':
                res.append(i)
            else:
                del res[-1]
        return "".join(res)

