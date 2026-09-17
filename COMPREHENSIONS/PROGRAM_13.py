#13. dictionary where each student is mapped to distinction,pass or fail
n = int(input())
marks = {}
for i in range(n):
    name = input()
    mark = int(input())
    marks[name] = mark
result = {
    name: "Distinction" if mark >= 75
    else "Pass" if mark >= 40
    else "Fail"
    for name, mark in marks.items()
}
print(result)