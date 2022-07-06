from db import User, Post, session

new_user1 = User(username="user1", email="user1@email.com")
new_user2 = User(username="user2", email="user2@email.com")
new_post = Post(title="sample title",
                content="this is sample content for our post")
new_post.author = new_user1

session.add_all([new_user1, new_user2, new_post])

new_post2 = Post(title="second post",
                 content="This is the second post", author=new_user1)
new_post3 = Post(title="third post",
                 content="This is the third post", author=new_user1)

session.add_all([new_post2, new_post3])

session.commit()

# Query
session.query(User).all()
session.query(Post).all()
session.query(Post.title).all()

