class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        row_freq = defaultdict(set)
        col_freq = defaultdict(set)
        subbox_freq = defaultdict(set)

        i = j = k = 0
        while i < rows:
            #For every square, it belongs to a column, row and sub-box
            square_ij = board[i][j]
            if square_ij != ".":
                if square_ij not in row_freq[i]:
                    row_freq.get(i).add(square_ij)
                else:
                    return False 
                if square_ij not in col_freq[j]:
                    col_freq.get(j).add(square_ij)
                else:
                    return False
                subbox_index = int((i // 3) * 3 + (j // 3)) # Subbox Index of square_ij
                if square_ij not in subbox_freq[subbox_index]:
                    subbox_freq.get(subbox_index).add(square_ij)
                else:
                    return False
            # Proceed to next square
            if j == 8:
                j = 0
                i += 1
            else:
                j += 1

        return True

            
                