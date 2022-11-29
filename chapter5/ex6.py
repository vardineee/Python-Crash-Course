current_users = ['nala', 'teri', 'jhone', 'emma', 'doe']
new_users = ['emma', 'oliver', 'nala', 'ameli', 'liam']
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"{user} is taken.")
    else:
        print(f"{user} is still available.")