class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        value_to_indices = defaultdict(list)
        
        for i, num in enumerate(nums):
            value_to_indices[num].append(i)
        
        count = 0
        
        for indices in value_to_indices.values():
            m = len(indices)
            if m < 2:
                continue
                
            for a in range(m):
                for b in range(a + 1, m):
                    i, j = indices[a], indices[b]
                    if (i * j) % k == 0:
                        count += 1
        
        return count
