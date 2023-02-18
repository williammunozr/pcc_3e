uncomfirmed_users = ['alice', 'brian', 'candance']
confirmed_users = []

while uncomfirmed_users:
    current_user = uncomfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# display all confirmed users.
print("\nThe following users have been conformed:")
for user in confirmed_users:
    print(user.title())