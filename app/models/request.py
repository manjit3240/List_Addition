from pydantic import BaseModel
from typing import List

class AdditionRequest(BaseModel):
    batchid: str
    payload: List[List[int]]

