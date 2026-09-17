#9. dictionary containing students who passed using dictionary comprehension
n = int(input())
students = {}
for i in range(n):
    name = input()
    mark = int(input())
    students[name] = mark
result = {
    name: mark
    for name, mark in students.items()
    if mark >= 40
}
print(result)