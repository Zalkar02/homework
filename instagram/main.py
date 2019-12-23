from post import *
from user import *


user = User("testuser", "testbio")
user.login()
post = Post(user, "testdescr")
user2 = User("pythoneast", "python")
user2.login()
post2 = Post(user2, "testdescr2")

user.like(post)
user2.like(post)
user.like(post2)
print(post2.likes)
print(post2.likes_amout())
print(post.likes)
print(post.likes_amout())


#comment = input("Enter ur comment: ")
#user2.comment(post, comment)
#print(post.comments, post.user)



user3 = User("user3", "user3")
user4 = User("user4", "user4")
user5 = User("user5", "user5")
user6 = User("user6", "user6")
user7 = User("user7", "user7")

user.follow(user2)
user.follow(user3)
user.follow(user4)
user.follow(user5)
user.follow(user6)
user.follow(user7)

# print(user.followings)

for u in user.followings:
    print(u.username)

user.unfollow(user4)
print(user4.followings)

user._User__save(post)
print(user._User__bookmarks[0].descr)


user._User__remove(post)
print(user._User__bookmarks)

user3._User__redact('Zak', 'pythoneast')
print(user3)