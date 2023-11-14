from typing import Optional
from pydantic import BaseModel

class CoinChange:
    def __init__(self,):
        pass

    class Input(BaseModel):
        inputs: Optional[list] = None

    class Output(BaseModel):
        answer: Optional[list] = None

    def countWays(self,coins, n, sum):

        dp = [0 for k in range(sum+1)]
        dp[0] = 1
        for i in range(0, n):
            for j in range(coins[i], sum+1):
                dp[j] += dp[j-coins[i]]
    
        return dp[sum]

   
    def solve(self,input):
        ans=0
        sum,n = list(map(int,input[0].split(' ')))
        coins = list(map(int,input[1].split(' ')))
        return self.countWays(coins,n,sum)
        