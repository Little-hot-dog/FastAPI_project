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

@app.get("/get-system-info/")
async def get_system_info(limit: int = 10, db: Session = Depends(get_db)):
    data = db.query(SystemInfo).limit(limit).all()
    return data


@app.get("/get-system-info/{id}")
async def get_system_info(id: Annotated[int, Path(..., title="Укажите id", ge=1)],
                          db: Session = Depends(get_db)):
    data = db.query(SystemInfo).filter(SystemInfo.id == id).first()
    if SystemInfo is None:
        return HTTPException(status_code=404, detail="Такой id не найден")
    return data


@app.delete("/delete-raw-and-system-info/{id}")
async def delete_data(id: Annotated[int, Path(..., title="Укажите id", ge=1)],
                      db: Session = Depends(get_db)):
    sys_info = db.query(SystemInfo).filter(SystemInfo.id == id).first()
    if sys_info:
        db.delete(sys_info)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Такой id не найден")

    raw_data = db.query(SystemInfo).filter(RawData.id == id).first()
    if raw_data:
        db.delete(raw_data)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Такой id не найден")



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