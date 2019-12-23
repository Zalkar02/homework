class User:
    def __init__(self, username, bio):
        self.username = username
        self.bio = bio
        self.aut = False
        self.followers = []
        self.followings = []
        self.__bookmarks = []

    def __str__(self):
        return self.username

    def login(self):
        self.aut = True

    def like(self, post_obj):
        if self.aut:
            post_obj.likes.append(self.username)
        else:
            print("u are not aut")

    def comment(self, post_obj, user_input):
        if self.aut:
            post_obj.comments[self.username] = user_input
        else:
            print("u are not aut")

    def follow(self, user_obj):
        user_obj.followers.append(self)
        self.followings.append(user_obj)

    def unfollow(self, user_obj):
        user_obj.followers.remove(self)
        self.followings.remove(user_obj)

    def __save(self, post_obj):
        self.__bookmarks.append(post_obj)

    def __remove(self, post_obj):
        self.__bookmarks.remove(post_obj)

    def __redact(self, name, bio):
    	self.username = name
    	self.bio = bio