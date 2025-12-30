class Solution {
    public int numMagicSquaresInside(int[][] grid) {
        int r = grid.length;
        int c = grid[0].length;
        int count = 0;
        for (int i = 0; i + 2 < r; i++) {
            for (int j = 0; j + 2 < c; j++) {
                if (isMagic(grid, i, j)) count++;
            }
        }
        return count;
    }

    private boolean isMagic(int[][] g, int r, int c) {
        boolean[] seen = new boolean[10];
        for (int i = r; i < r + 3; i++) {
            for (int j = c; j < c + 3; j++) {
                int v = g[i][j];
                if (v < 1 || v > 9 || seen[v]) return false;
                seen[v] = true;
            }
        }

        int s = g[r][c] + g[r][c + 1] + g[r][c + 2];

        for (int i = 0; i < 3; i++) {
            if (g[r + i][c] + g[r + i][c + 1] + g[r + i][c + 2] != s) return false;
            if (g[r][c + i] + g[r + 1][c + i] + g[r + 2][c + i] != s) return false;
        }

        if (g[r][c] + g[r + 1][c + 1] + g[r + 2][c + 2] != s) return false;
        if (g[r][c + 2] + g[r + 1][c + 1] + g[r + 2][c] != s) return false;

        return true;
    }
}
