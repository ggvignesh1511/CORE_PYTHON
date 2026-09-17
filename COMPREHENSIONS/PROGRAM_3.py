#3. Pass/Fail using List Comprehensions
l = list(map(int, input().split()))
result = ["Pass" if i>=40 else "Fail" for i in l]
print(result)