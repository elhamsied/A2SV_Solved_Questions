class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        
        for size in range(len(arr), 1, -1):
            max_i = arr.index(max(arr[:size]))
            
            if max_i != size - 1:
                if max_i != 0:
                    res.append(max_i + 1)
                    arr[:max_i+1] = reversed(arr[:max_i+1])
                
                res.append(size)
                arr[:size] = reversed(arr[:size])
        
        return res