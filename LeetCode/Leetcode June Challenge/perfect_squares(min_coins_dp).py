def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1,int(n**0.5)+1)]
        dp = [float('inf') for i in range(n+1)]
        dp[0] = 0
        for i in squares:
            for j in range(1,n+1):
                if j >= i:
                    dp[j] = min(dp[j - i]+1, dp[j])
        return dp[-1]
