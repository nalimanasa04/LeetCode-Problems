import java.util.*;

class Solution {
    public int latestDayToCross(int row, int col, int[][] cells) {
        int left = 1, right = cells.length, ans = 0;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (canCross(row, col, cells, mid)) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return ans;
    }

    private boolean canCross(int row, int col, int[][] cells, int day) {
        int[][] grid = new int[row][col];
        for (int i = 0; i < day; i++) {
            grid[cells[i][0] - 1][cells[i][1] - 1] = 1;
        }
        Queue<int[]> q = new ArrayDeque<>();
        boolean[][] vis = new boolean[row][col];
        for (int j = 0; j < col; j++) {
            if (grid[0][j] == 0) {
                q.offer(new int[]{0, j});
                vis[0][j] = true;
            }
        }
        int[] d = {0, 1, 0, -1, 0};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];
            if (r == row - 1) return true;
            for (int k = 0; k < 4; k++) {
                int nr = r + d[k], nc = c + d[k + 1];
                if (nr >= 0 && nr < row && nc >= 0 && nc < col && !vis[nr][nc] && grid[nr][nc] == 0) {
                    vis[nr][nc] = true;
                    q.offer(new int[]{nr, nc});
                }
            }
        }
        return false;
    }
}
