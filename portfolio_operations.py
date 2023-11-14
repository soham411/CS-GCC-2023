from typing import Optional
from pydantic import BaseModel

class PortfolioOp:
    class Input(BaseModel):
        inputs: Optional[Optional[list]] = None

    class Output(BaseModel):
        answer: Optional[list] = None

    @staticmethod
    def solve(input):
        ans=0
        n,m,maxSum = list(map(int,input[0].split(' ')))
        a,ai = list(map(int,input[1].split(' '))),0
        b,bi = list(map(int,input[2].split(' '))),0
        rsum =0
        while ai < n and bi < m:
            if a[ai] < b[bi]:
                if (rsum + a[ai]) <= maxSum:
                    rsum += a[ai]
                    ai +=1
                    ans +=1
                else:
                    break
            else:
                if (rsum + b[bi]) <= maxSum:
                    rsum += b[bi]
                    bi +=1  
                    ans +=1
                else:
                    break
        
        while ai < n:
            if (rsum + a[ai]) <= maxSum:
                    rsum += a[ai]
                    ai +=1
                    ans +=1
            else:
                break

        while bi < m:
            if (rsum + b[bi]) <= maxSum:
                    rsum += b[bi]
                    bi +=1  
                    ans +=1
            else:
                break



        return ans
                