class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
    

        def backtrack(first_num, curr):
            if len(curr) == k:
                ans.append(curr[:])
                return

            need = k - len(curr)
            max_pick = n - need + 1 
            for num in range(first_num, n + 1):
                curr.append(num)
                backtrack(num + 1, curr)
                curr.pop()

        ans = []
        backtrack(1, [])
        return ans
