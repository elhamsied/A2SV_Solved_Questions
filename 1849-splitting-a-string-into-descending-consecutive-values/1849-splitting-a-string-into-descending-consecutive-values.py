class Solution:
    def splitString(self, s: str) -> bool:
        def split(idx,prev):
            if idx == len(s):
                return True
            num = 0
            for i in range(idx,len(s)):
                num = num*10 + int(s[i])
                if num == prev -1:
                    if split(i + 1, num):
                        return True
                elif num >= prev:
                    break
            return False

        for i in range(1, len(s)):
            first = int(s[:i])
            if split(i, first):
                return True
        
        return False