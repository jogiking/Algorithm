class Solution:
    def numTrees(self, n: int) -> int:
        """
        n=1 -> 1 (0)
        n=2 -> 2 (1,0),(0,1)
        n=3 -> 5 (0,2),(2,0), (1,1), = 1*s(2) + s(1)*s(1) + s(2)*1 = 2+1+2
        n=4 ->   (3,0),(0,3), (1,1) = s(3)*1 + s(3)*1 + s(1)*s(2)+s(2)*s(1)
        
        Sn = S0*Sn-1 + S1*Sn-2 + S2*Sn-3 ... Sn-3*S2 + Sn-2*S1 + Sn-1*S0        
        S2 = S0*S1 + S1*S0
        
        dp4 = dp3*dp0 + dp2*dp1 + dp1*dp2 + dp0*dp3
        """
        
        dp = [0]*(n+1)
        dp[0]=1
        dp[1]=1
        
        for i in range(2,n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        
        return dp[n]
        