class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        agreed = [0] * (n + 1) 
        for start, end, k in shifts:
            if k == 1:
                shift_to = 1 
            else:
                shift_to = -1
            agreed[start] += shift_to
            if end + 1 < n:
                agreed[end + 1] -= shift_to
                
        total_shift = [0] * n
        pri = 0
        for i in range(n):
            pri += agreed[i]
            total_shift[i] = pri
        s= list(s) 
    
        for i in range(n):
            char = ord(s[i]) - ord('a')

            new = (char + total_shift[i]) % 26
            
            s[i] = chr(new + ord('a'))
        return "".join(s)
