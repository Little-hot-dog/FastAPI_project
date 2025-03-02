from pydantic import BaseModel
from typing import List


from sqlalchemy import Column, Integer, String, ForeignKey, JSON, DateTime


class RawDataRequest(BaseModel):
    data: List[dict]

class SystemInfoResponse(BaseModel):
    id: int
    host: str
    param: str
    value: str