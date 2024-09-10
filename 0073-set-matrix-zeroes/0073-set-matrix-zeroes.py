class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        findZero = {}

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    findZero[(row,col)] = True

        for (row, col) in findZero:
            for i in range(cols):
                matrix[row][i] = 0

            for j in range(rows):
                matrix[j][col] = 0
                
        


        


        