class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s) 
        for i in range(len(s) - 1):
            char1 = s[i]
            char2 = s[i + 1]
            
            val1 = int(char1)
            val2 = int(char2)
            if val1 != val2 and count[char1] == val1 and count[char2] == val2:
                return char1 + char2
                
        return ""
