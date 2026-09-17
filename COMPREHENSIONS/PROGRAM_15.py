#15. create a dictionary using dictionary comprehension for pass/fail
names = input().split()
marks = list(map(int, input().split()))
result = {
    names[i]: "Pass" if marks[i] >= 40 else "Fail"
    for i in range(len(names))
}
print(result)