from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQl_DB_URL = "postgresql://postgres:12341234@localhost/mydatabase"

engine = create_engine(SQl_DB_URL, echo=True)
    #echo = True - все взаимодействия с БД будут отображаться в консоли

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()