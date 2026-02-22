class Comment:

    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes

comment = Comment(username='Mara',content='zero',likes=0)

print(comment.username)