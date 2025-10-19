# Users database (id -> user info)
fake_users_db = {
    1: {"id": 1, "username": "krishna", "email": "krishna@example.com"},
    2: {"id": 2, "username": "kallu", "email": "kallu@example.com"}
}

# Posts database (list of posts)
fake_posts_db = [
    {"id": 1, "text": "Hello world!", "owner_id": 1},
    {"id": 2, "text": "Kallu's first post!", "owner_id": 2}
]

# Likes database (list of likes)
fake_likes_db = [
    {"post_id": 1, "user_id": 2}  # Kallu liked Krishna's post
]

# Comments database (list of comments)
fake_comments_db = [
    {"post_id": 1, "user_id": 2, "text": "Nice post Krishna!"}
]
