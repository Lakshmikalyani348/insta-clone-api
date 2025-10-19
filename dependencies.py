from fastapi import Header, HTTPException
from insta_clone_api import database

# Dependency to get current user
def get_current_user(x_user_id: int = Header(...)):
    # Check if user exists in our fake DB
    user = database.fake_users_db.get(x_user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
