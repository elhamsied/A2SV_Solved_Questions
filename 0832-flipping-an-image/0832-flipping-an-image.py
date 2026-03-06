class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        
        for row in image:
            row = row[::-1]
            row = [1 - x for x in row]  # invert
            result.append(row)
        return result