from .. import model, schemas
from fastapi import FastAPI, Response,status,HTTPException,Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List



router =APIRouter(
    prefix = "/posts",
    tags=['Posts']
)

@router.get("/",response_model=List[schemas.Post])
def get_post(db: Session = Depends(get_db)):
    post = db.query(model.Post).all()
    return post
    ##cursor.execute("SELECT * FROM posts")
    ##posts = cursor.fetchall()
    ##return {"data" : posts}


@router.post("/", status_code = status.HTTP_201_CREATED,response_model=schemas.Post)
# Body is convert into dictionary variable name payload
def create_posts(post:schemas.PostCreate,db: Session = Depends(get_db)):
    #cursor.execute("INSERT INTO posts(title,content,is_published) VALUES(%s,%s,%s) RETURNING *",(post.title,post.content,post.published))
    #new_post = cursor.fetchone()
    #conn.commit()
    new_post=model.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
# title str, content str, category, Bool published 

@router.get("/{id}",response_model=schemas.Post)
def get_post(id : int,db: Session = Depends(get_db)):
    #cursor.execute("SELECT * FROM posts WHERE id = %s",str(id))
    #post = cursor.fetchone()
    post = db.query(model.Post).filter(model.Post.id ==id).first()
    if not post: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"post with id: {id} was not found")
    return post


@router.delete("/{id}",status_code = status.HTTP_204_NO_CONTENT)
def delete_posts(id:int,db: Session = Depends(get_db)):
    #cursor.execute("DELETE FROM posts WHERE id = %s RETURNING * ",str(id)) 
    #post=cursor.fetchone()
    post_query = db.query(model.Post).filter(model.Post.id ==id)
    
    if not post_query.first(): 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"post with id: {id} was not found")
    db.delete(post_query.first())
    db.commit()
    #conn.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)
    
@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int, update_post: schemas.PostCreate,db: Session = Depends(get_db)):
    #cursor.execute("UPDATE posts SET title = %s, content = %s, is_published = %s  WHERE id = %s RETURNING *",(post.title,post.content,post.published,str(id)))
    #updated_post = cursor.fetchone()
    post_query = db.query(model.Post).filter(model.Post.id ==id)
    post = post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with the id {id} does not exist")
    #conn.commit()
    post_query.update(update_post.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()
