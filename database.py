from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# format SQLALCHEMY_DATABASE_URL = 'postgresql://<username>;<password>@<ip-address/hostname>/<dadtabase_name>'
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:3204@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()