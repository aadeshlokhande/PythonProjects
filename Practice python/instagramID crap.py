#pip install instapy
from instagramy import InstagramUser
# Author = TECH_IN_SECONDS

id = input("Enter a Instagram Username = ")
user = InstagramUser(id.lower())
print('\nFullname\t=',user.fullname)
print('username\t=',user.username)
print('Followers\t=',user.number_of_followers)
print('Following\t=',user.number_of_followings)
print('Posts\t\t=',user.number_of_posts)
print('Private\t\t=',user.is_private)
print('Verified\t=',user.is_verified)
print('\nBio: \n',user.biography)


# Enter a Instagram Username = tech_in_seconds

# Fullname        = Tech_In_Seconds
# username        = tech_in_seconds
# Followers       = 2726
# Following       = 1335
# Posts           = 17
# Private         = False
# Verified        = False

# Bio: 
#  π€ print("Welcome programmers") π€
# π» I'm Python Lover π»
# π±Android & πΈ Web Development
# π€ Freelancer π€
#   π Brand Promotion π
# π Degital Marketing π