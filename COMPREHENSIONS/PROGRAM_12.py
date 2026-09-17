#12. generator that produces only numbers greater than 20
numbers = list(map(int, input().split()))
gen = (i for i in numbers if i > 20)
for i in gen:
    print(i)