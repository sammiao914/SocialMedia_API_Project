from .database import Base
from sqlalchemy import Column, Integer,String,Boolean
from sqlalchemy.sql.expression import text,null
from sqlalchemy.sql.sqltypes import TIMESTAMP
class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True,nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean,server_default='TRUE',nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'),nullable=False)
class User(Base):
    __tablename__ = "user"
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    id = Column(Integer, primary_key=True,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'),nullable=False)