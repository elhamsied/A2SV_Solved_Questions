class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        letters=Counter(s1+s2)
        for v in letters.values():
            if v%2:
                return -1

        count=Counter()
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                count[s1[i]+s2[i]]+=1 
        ans=0
        for value in count.values():
            if value%2:
                ans+=((value//2)+1)
            else:
                ans+=(value//2)
        return ans