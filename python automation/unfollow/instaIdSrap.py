# # pip install instaloader
# from instaloader import Instaloader

# loader = Instaloader()
# username = "aadesh_lokhande"
# loader.download_profile(username, profile_pic_only= True)

 # Get instance
import instaloader
insta = instaloader.Instaloader()

# Login or load session
insta.login("asian_girls_villa", input("Enter pass = "))        # (login)
#L.load_session_from_file(myaccount)


username = input("Enter username = ")

# Obtain profile metadata
profile = instaloader.Profile.from_username(insta.context, username)

# Print list of followers

follow_list = []
count=0

file = open(f"{username}_Followers.txt","a+")
for follower in profile.get_followers():
    user = follower.username
    # name = follower.full_name
    # flwrs = follower.followers
    # private = follower.is_private
    # verify = follower.is_verified
    # data = f"['{name}','https://www.instagram.com/{user}','{flwrs}','{private}','{verify}' ]\n"
    file.write(f"{user}\n")
    print(user)
file.close()
