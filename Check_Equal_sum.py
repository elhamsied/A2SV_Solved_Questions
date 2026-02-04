class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        x = sorted(a)
        y = sorted(b)
        return x == y
