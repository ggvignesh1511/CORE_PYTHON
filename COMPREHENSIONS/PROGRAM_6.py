#6. Student pass/fail using Dictionary Comprehensions
n = int(input())
students = {}
for i in range(n):
    name, mark = input().split()
    students[name] = int(mark)
result = {
    name: "Pass" if mark >= 40 else "Fail"
    for name, mark in students.items()
}
print(result)