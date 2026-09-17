#7. username mapped to password using Dictionary Comprehensions
usernames = input().split()
passwords = input().split()
result = {
    usernames[i]: passwords[i]
    for i in range(len(usernames))
}
print(result)