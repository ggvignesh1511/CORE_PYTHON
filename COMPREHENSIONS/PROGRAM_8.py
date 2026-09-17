#8. dictionary where the value is either "Expensive" or "Affordable"
n = int(input())
products = {}
for i in range(n):
    name = input()
    price = int(input())
    products[name] = price
result = {
    name: "Expensive" if price > 10000 else "Affordable"
    for name, price in products.items()
}
print(result)