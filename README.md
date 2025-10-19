# insta-clone-apI

A simple Instagram clone backend API built with FastAPI.  
Supports creating posts, liking posts, commenting, and deleting posts.



## Technologies Used
- Python 3.10
- FastAPI
- Uvicorn
- Pydantic

---

## Project Structure
insta_clone_api/
├── main.py
├── database.py
├── dependencies.py
├── schemas.py
├── routers/
│ └── posts.py

Running the API
API Endpoints
Posts

POST /posts/ → Create Post

GET /posts/ → Get All Posts

DELETE /posts/{post_id} → Delete Post

POST /posts/like → Like Post

POST /posts/comment → Comment Post



Start the server with:

uvicorn insta_clone_api.main:app --reload

Visit the API docs at http://127.0.0.1:8000/docs

linkedin id: https://www.linkedin.com/posts/lakshmi-kalyani-rasamsetti-404920316_python-fastapi-backenddevelopment-activity-7385699646762934272-O5Bs?utm_source=social_share_video_v2&utm_medium=android_app&rcm=ACoAAFA58EQB57jB3kXyZhFizvrJ6xHXHu1_MQ4&utm_campaign=copy_link
