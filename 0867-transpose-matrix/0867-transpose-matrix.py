class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
         result = []
        
         for j in range(len(matrix[0])):   
            new_row = []
            for i in range(len(matrix)):  
                new_row.append(matrix[i][j])
            result.append(new_row)
        
         return result