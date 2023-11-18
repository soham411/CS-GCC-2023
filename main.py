from typing import Optional
from fastapi import FastAPI
from fraudulent_transactions import FraudTransact
from portfolio_operations import PortfolioOp
from pydantic import BaseModel
from file_reorganization import FileReorg
from coin_change import CoinChange
from risk_mitigation import RiskMitigation
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

@app.post("/portfolio-operations",response_model=PortfolioOp.Output)
async def file_reorganization(input : PortfolioOp.Input):
    ans=[]
    
    for i in input.inputs:        
        ans.append(PortfolioOp.solve(i))

    return {"answer":ans}

@app.post("/coin-change",response_model=CoinChange.Output)
async def coin_change(input : CoinChange.Input):
    ans=[]
    
    for i in input.inputs:
        
        ans.append(CoinChange().solve(i))

    return {"answer":ans}

@app.post("/risk-mitigation",response_model=RiskMitigation.Output)
async def risk_mitigation(input : RiskMitigation.Input):
    ans=[]
    
    for i in input.inputs:
        
        ans.append(RiskMitigation().solve(i))


    return {"answer":ans}

@app.post("/fraudulent-transactions",response_model=FraudTransact.Output)
async def fraudulent_transactions(input : FraudTransact.Input):
    ans=[]
    
    for i in input.inputs:
        ans.append(FraudTransact().solve(i))

    return {"answer":ans}