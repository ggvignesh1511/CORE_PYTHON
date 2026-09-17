#14. dictionary where each username is valid or invalid
usernames = input().split()
result = {
    username: "Valid" if len(username) >= 5 else "Invalid"
    for username in usernames
}
print(result)