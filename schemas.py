from pydantic import BaseModel
from typing import List

# class RawDataRequest(BaseModel):
#     data: dict

class RawDataRequest(BaseModel):
    data: List[dict]