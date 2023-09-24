#Pascal Triangle
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0 for i in range(101)] for j in range(101)]
        dp[0][0] = float(poured)  # Pour all champagne into the first glass
        for i in range(query_row + 1):
            for j in range(i + 1):
                overflow = (dp[i][j] - 1.0) / 2.0  # Calculate overflow
                if overflow > 0:
                    dp[i + 1][j] += overflow  # Distribute overflow to the glass below
                    dp[i + 1][j + 1] += overflow  # Distribute overflow to the glass below and to the right
        return min(1.0, dp[query_row][query_glass])
