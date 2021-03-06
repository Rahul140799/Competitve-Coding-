dp = [ [0 for j in range(len(word2)+1)] for i in range(len(word1)+1) ]
        
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i  
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
        
        return dp[-1][-1]
