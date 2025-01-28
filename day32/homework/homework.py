# 2) Reverse List with While Loop
numbers = [1, 2, 3, 4, 5]
reversed_list = []

while numbers:
    reversed_list.append(numbers.pop())
print("2) შებრუნებული სია:", reversed_list)

# 3) Filter Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print("3) ლუწი რიცხვების სია:", even_numbers)

# 4) Find Maximum with For Loop
numbers = [1, 546, 456, 123]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
print("4) მაქსიმალური რიცხვი:", maximum)

# 5) Find Minimum with For Loop
minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num
print("5) მინიმალური რიცხვი:", minimum)

# 6) Filter Odd Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = []

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
print("6) კენტი რიცხვების სია:", odd_numbers)

# 7) Sum of Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_even = sum(num for num in numbers if num % 2 == 0)
print("7) ლუწი რიცხვების ჯამი:", sum_even)

# Print sum_even 10 times
for _ in range(10):
    print(f"ლუწი რიცხვების ჯამი (10-ჯერ): {sum_even}")

# 8) Sum of Odd Numbers
sum_odd = sum(num for num in numbers if num % 2 != 0)
print("8) კენტი რიცხვების ჯამი:", sum_odd)

# Print sum_odd 10 times
for _ in range(10):
    print(f"კენტი რიცხვების ჯამი (10-ჯერ): {sum_odd}")

# 9) While Loop with Counter
counter = 0

while counter < 50:
    counter += 1
    print(f"Loop {counter}")
    if counter == 47:
        print("9) ლუპი გაჩერდა 47-ზე.")
        break
