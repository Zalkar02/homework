class Post:
    def __init__(self, user, descr):
        self.user = user
        self.descr = descr
        self.likes = []
        self.comments = {}

    def __str__(self):
        return self.descr


    def likes_amout(self):
        return len(self.likes)