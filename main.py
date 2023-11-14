from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from file_reorganization import FileReorg
# from Inputs import Inputs
app = FastAPI()

class Item(BaseModel):
    inputs: Optional[list] = None
    
class Output:
    def __init__(self):
        self.inputs = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/file-reorganization",response_model=FileReorg.Output)
async def file_reorganization(input : FileReorg.Input):
    ans=[]
    for s in input.inputs:
        ans.append(FileReorg.solve(s))

    return {"answer":ans}