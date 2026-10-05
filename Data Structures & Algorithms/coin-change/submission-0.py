class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            temp_min = 0
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)
        
        return dp[amount] if dp[amount] < sys.maxsize else -1