from typing import Optional
from pydantic import BaseModel

class FileReorg:
    class Input(BaseModel):
        inputs: Optional[list] = None

    class Output(BaseModel):
        answer: Optional[list] = None

    @staticmethod
    def solve(s):
        ans =0
        ch = {}
        for c in s:
            if c in ch.keys():
                ch[c] += 1
            else:
                ch[c] = 1
        inc =0
        for k in ch.keys():
            if ch[k] == 1 and inc == 0:
                inc += 1
            else:
                ans+= (ch[k] // 2) * 2

        return ans + inc