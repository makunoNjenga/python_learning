for item in "Pythorn":
    print(item)

for item in ['pythorn', 'java', 'c++', 'laravel']:
    print(item)

for item in [1, 2, 3, 3, 4, 5]:
    print(item)

for item in range(2, 10):
    print(item)

for item in range(2, 10, 3):
    print(item)

# exercise
prices = [100, 12, 34, 45, 67, 28, 9, 287, 99]
total_price = 0
for price in prices:
    total_price += price
print("\n----------EXERCISE------------")
print(f"Total prices in a shopping cart is ${total_price}")
