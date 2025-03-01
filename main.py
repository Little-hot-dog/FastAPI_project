from fastapi import FastAPI, HTTPException, Path, Query, Body, Depends
from typing import Optional, List, Dict, Annotated
from sqlalchemy.orm import Session

from models import Base, RawData, SystemInfo
from database import engine, session_local
from schemas import RawDataRequest


app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.post("/post-raw-data/")
async def create_raw_data(raw_data: RawDataRequest, db: Session = Depends(get_db)):
    for item_data in raw_data.data:
        db_raw_data = RawData(data=item_data)
        db.add(db_raw_data)
        db.commit()
        db.refresh(db_raw_data)

        distribution_to_table(db_raw_data.data, db)

    return raw_data

def distribution_to_table(data: dict, db: Session):
    system_info = SystemInfo(
        host = data.get('host'),
        dhcp = data.get('dhcp')
    )
    db.add(system_info)
    db.commit()
    db.refresh(system_info)

# @app.post("/post-raw-data/")
# async def create_raw_data(raw_data: RawDataRequest, db: Session = Depends(get_db)):
#
#     db_raw_data = RawData(data=raw_data.data)
#     db.add(db_raw_data)
#     db.commit()
#     db.refresh(db_raw_data)
#
#     distribution_to_table(db_raw_data.data, db)
#
#     return raw_data