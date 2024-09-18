import instaloader
import getpass

L = instaloader.Instaloader()

#Placeholder
username = input("Enter Instagram username: ")
password = getpass.getpass("Enter Instagram password: ")

L.login(username, password)

profile = instaloader.Profile.from_username(L.context, username)

followees = set(profile.get_followees())
followers = set(profile.get_followers())

not_followed_by = followees - followers
not_following = followers - followees

print(f"Number of people you follow but don't follow you back: {len(not_followed_by)}")
for idx, user in enumerate(not_followed_by, 1):
    print(f"{idx}. Not following back: {user.username}")

print(f"\nNumber of people who follow you but you don't follow back: {len(not_following)}")
for idx, user in enumerate(not_following, 1):
    print(f"{idx}. You're not following back: {user.username}")