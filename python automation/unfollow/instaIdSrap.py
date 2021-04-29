# # pip install instaloader
# from instaloader import Instaloader

# loader = Instaloader()
# username = "aadesh_lokhande"
# loader.download_profile(username, profile_pic_only= True)

 # Get instance
import instaloader
insta = instaloader.Instaloader()

# Login or load session
insta.login("asian_girls_villa", "Asian786")        # (login)
#L.load_session_from_file(myaccount)


# Obtain profile metadata
profile = instaloader.Profile.from_username(insta.context, "i_know_python")

# Print list of followers


file = open(f"DataFollowers.txt","a+")
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
