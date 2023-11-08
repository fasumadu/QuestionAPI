from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#connection string for sqlalchemy
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Descend175@localhost/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


#sending any api request we use this:db:session=depends(get_db)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

