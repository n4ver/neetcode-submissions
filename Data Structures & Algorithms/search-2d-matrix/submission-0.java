class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;

        int x = 0;
        int y = m*n - 1;
        while (x <= y) {
            int middle = x + (y-x)/2;
            int midRow = middle / n;
            int midCol = middle % n;
            if (matrix[midRow][midCol] < target) x = middle + 1;
            else if (matrix[midRow][midCol] > target) y = middle - 1;
            else return true;
        }
        return false;
    }
}
