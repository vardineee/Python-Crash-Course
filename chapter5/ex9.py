banned_users = ['andrew', 'carolina', 'david']
user ='andrew'
if user not in banned_users:
    print(f"{user.title()} please post response")
elif user in banned_users:
    print("Tanks")
