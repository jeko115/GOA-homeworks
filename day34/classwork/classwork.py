import random

# სიის შექმნა 10 შემთხვევითი რიცხვისგან (1-100 დიაპაზონი)
numbers = [random.randint(1, 100) for _ in range(10)]

# ჯამი
total = 0
for num in numbers:
    total += num

# დაბეჭდვა
print("რიცხვები:", numbers)
print("ჯამი:", total)
