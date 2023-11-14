from typing import Optional
from pydantic import BaseModel

class RiskMitigation:
    def __init__(self,):
        pass

    class Input(BaseModel):
        inputs: Optional[list] = None

    class Output(BaseModel):
        answer: Optional[list] = None

    def max_profit(self,price, n, k):
        profit = [0] * (k + 1)
        prev_diff = [float('-inf')] * (k + 1)

        # Fill the table in bottom-up fashion
        for j in range(n):
            for i in range(1, k + 1):
                prev_diff[i] = max(prev_diff[i], profit[i - 1] - price[j])
                profit[i] = max(profit[i], price[j] + prev_diff[i])
 
        return profit[k]

   
    def solve(self,input):
        ans=0
        n,m = list(map(int,input[0].split(' ')))
        costs = list(map(int,input[1].split(' ')))

        return self.max_profit(costs,m,n)
        