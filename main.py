from fastapi import FastAPI, Response,status,HTTPException,Depends
from fastapi.params import Body
from typing import Optional,List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time 
from sqlalchemy.orm import Session
from app.schemas import UserReponse
from . import model, schemas,utils
from .database import engine,get_db
from .routers import post, user,auth
# Go to cmd and use the virtual environemnt venv\Scripts\activate.bat 
# uvicorn app.main:app --reload


model.Base.metadata.create_all(bind=engine)
app = FastAPI()



# path operation
 # / means the root 
 # request Get method url :"/"
while True:
    try:
        conn = psycopg2.connect(host = 'localhost',database = 'fastapi',user ='postgres',password ='3204',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull")
        break
    except Exception as error:
        print("connection to database failed")
        print("Error",error)
        time.sleep(2)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)