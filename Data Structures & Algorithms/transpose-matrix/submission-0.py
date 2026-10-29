class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        transpose = [[0] * rows for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                transpose[c][r] = matrix[r][c]
        return transpose
        
        '''
            m >
          n 1  0  5
          v 2  4  3

        '''