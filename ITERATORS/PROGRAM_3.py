class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.num < self.n:
            self.num += 2
            return self.num
        raise StopIteration

n = int(input())
obj1 = EvenNumbers(n)
k = iter(obj1)
for i in k:
    print(i)
