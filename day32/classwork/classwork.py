import random

# სიის შექმნა 10 შემთხვევითი რიცხვით (1-100 დიაპაზონი)
numbers = [random.randint(1, 100) for _ in range(10)]

# სიის თითოეული ელემენტის დამუშავება
for num in numbers:
    message = f"{num}"  # სტარტი - რიცხვის ბეჭდვა
    if num % 5 == 0:
        message += " - ხუთის ჯერადია"
    if num % 3 == 0:
        message += " - სამის ჯერადია"
    print(message)
