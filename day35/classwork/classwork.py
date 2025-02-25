import random

numbers = random.sample(range(1, 100), 10)  
print("რიცხვების სია:", numbers)

total = 0
for num in numbers:
    total += num

print("რიცხვების ჯამი:", total)
