#11. generator that generates only even numbers from 1 to 20
gen = (i for i in range(1, 21) if i % 2 == 0)
for i in gen:
    print(i)