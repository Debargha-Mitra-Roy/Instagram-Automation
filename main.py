from instabot import Bot

bot = Bot()


# Login
user_name = input("Enter the username : ")
pass_word = input("Enter the password : ")
bot.login(username=user_name, password=pass_word)


# Follow
follower_user_name = input("Enter the username, if you want to follow : ")
bot.follow(follower_user_name)


# Upload Photo
photo_path = input("Enter the full photo path : ")
bot.upload_photo(photo_path, caption="Uploaded Photo")


# Unfollow
unfollower_user_name = input("Enter the username, if you want to unfollow : ")
bot.unfollow(unfollower_user_name)


# Send same message to multiple users
input_message = input("Enter the message :\n")
senders = input("Enter the senders username :\n")
senders_list = senders.split()
# print("list : ", senders_list)
bot.send_message(input_message,  senders_list)


# Information about Followers
followers = bot.get_user_followers(user_name)
for follower in followers:
    print(bot.get_user_info(follower))


# Information about Followings
followings = bot.get_user_following(user_name)
for following in followings:
    print(bot.get_user_info(following))
