class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        count = Counter(changed)
        total = []
        
        for x in sorted(count):
            if count[x] > count[2 * x]:
                return []
            if x == 0:
                if count[x] % 2 != 0:
                    return []
                total.extend([0] * (count[x] // 2))
                count[x] = 0
            else:
                total.extend([x] * count[x])
                count[2 * x] -= count[x]
                count[x] = 0
        
        return total