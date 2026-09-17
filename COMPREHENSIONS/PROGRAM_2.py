#2. Squares of all numbers using List Comprehensions
l = list(map(int, input().split()))
result = [i * i for i in l]
print(result)