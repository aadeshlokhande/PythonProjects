# # pip install instaloader
# from instaloader import Instaloader

# loader = Instaloader()
# username = "aadesh_lokhande"
# loader.download_profile(username, profile_pic_only= True)

 # Get instance
import instaloader
L = instaloader.Instaloader()

# Login or load session
L.login("asian_girls_villa", "Cool786")        # (login)
#L.load_session_from_file(myaccount)


# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, "i_know_python")

# Print list of followers

follow_list = []
count=0

# for follower in profile.get_followers():
#     file = open("uspython.txt","a+")
#     user = follower.username
#     # name = follower.full_name
#     # flwrs = follower.followers
#     # private = follower.is_private
#     # verify = follower.is_verified
#     # data = f"['{name}','https://www.instagram.com/{user}','{flwrs}','{private}','{verify}' ]\n"
#     file.write(f"{user}\n")
#     print(user)
#     file.close()
