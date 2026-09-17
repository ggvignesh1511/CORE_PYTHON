#5. Length of words using Set Comprehensions
l = input().split()
result = {len(i) for i in l}
print(result)