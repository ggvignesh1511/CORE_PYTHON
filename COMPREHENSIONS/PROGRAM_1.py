#1. Even Numbers using List Comprehensions
l = list(map(int, input().split()))
result = [i for i in l if i % 2 == 0]
print(result)