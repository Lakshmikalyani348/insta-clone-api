from pydantic import BaseModel

# --------- User Schema ---------
class User(BaseModel):
    id: int
    username: str
    email: str

# --------- Post Schemas ---------
class PostCreate(BaseModel):
    text: str

class Post(BaseModel):
    id: int
    text: str
    owner_id: int

# --------- Like Schema ---------
class Like(BaseModel):
    post_id: int
    user_id: int

# --------- Comment Schema ---------
class Comment(BaseModel):
    post_id: int
    user_id: int
    text: str


