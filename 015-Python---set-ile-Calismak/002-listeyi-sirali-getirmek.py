users = ["Duygu", "Derya", "Django", "Derya", "Duygu"]

print(set(users))


# new_users = {key:None for key in users}
new_users = list({key:None for key in users}.keys())

print(new_users)
