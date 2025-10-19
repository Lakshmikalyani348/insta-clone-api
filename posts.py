from fastapi import APIRouter, Depends, HTTPException, status
from .. import database, schemas, dependencies

router = APIRouter(prefix="/posts", tags=["posts"])


# 🟢 Create Post
@router.post("/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, current_user: dict = Depends(dependencies.get_current_user)):
    new_post = {
        "id": len(database.fake_posts_db) + 1,
        "text": post.text,
        "owner_id": current_user["id"]
    }
    database.fake_posts_db.append(new_post)
    return new_post


# 🟢 Get All Posts
@router.get("/", response_model=list[schemas.Post])
def get_all_posts():
    return database.fake_posts_db


# 🔴 Delete Post
@router.delete("/{post_id}")
def delete_post(post_id: int, current_user: dict = Depends(dependencies.get_current_user)):
    post = next((p for p in database.fake_posts_db if p["id"] == post_id), None)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    if post["owner_id"] != current_user["id"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this post")

    database.fake_posts_db.remove(post)
    return {"message": "Post deleted successfully"}


# 💙 Like Post
@router.post("/like")
def like_post(like: schemas.Like):
    database.fake_likes_db.append(like.dict())
    return {"message": "Post liked successfully"}


# 💬 Comment on Post
@router.post("/comment")
def comment_post(comment: schemas.Comment):
    database.fake_comments_db.append(comment.dict())
    return {"message": "Comment added successfully"}
