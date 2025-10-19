from fastapi import FastAPI
from insta_clone_api.routers import posts

# Create FastAPI app instance
app = FastAPI(title="Insta Clone API", version="1.0")

# Include posts router
app.include_router(posts.router)

# Root route
@app.get("/")
def home():
    return {"message": "Welcome to Insta Clone API!"}
