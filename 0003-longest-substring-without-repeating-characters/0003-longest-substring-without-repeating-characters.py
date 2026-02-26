class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = set()
        maximum = 0
        lft = 0
        for i in range(len(s)):
            while s[i] in win:
                win.remove(s[lft])
                lft +=1

            win.add(s[i])
            maximum = max(maximum,i-lft + 1)
        return maximum