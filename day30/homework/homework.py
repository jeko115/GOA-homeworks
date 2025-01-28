# 1. შექმენით ლისტი 1-10 ჩათვლით და დაპრინტეთ მხოლოდ ლუწი რიცხვები
numbers = list(range(1, 11))
even_numbers = [num for num in numbers if num % 2 == 0]
print("ლუწი რიცხვები:", even_numbers)

# 2. შექმენით ლისტი 1-10 ჩათვლით და დაპრინტეთ მხოლოდ კენტი რიცხვები
odd_numbers = [num for num in numbers if num % 2 != 0]
print("კენტი რიცხვები:", odd_numbers)

# 3. ყველა რიცხვი, მიუწერეთ კენტი თუ ლუწი
for num in numbers:
    if num % 2 == 0:
        print(f"{num} - ლუწი")
    else:
        print(f"{num} - კენტი")

# 4. შექმენით ლისტი და დაამატეთ მხოლოდ ლუწი რიცხვები ახალ ლისტში
even_list = [num for num in numbers if num % 2 == 0]
print("ახალი ლუწი რიცხვების ლისტი:", even_list)

# 5. შექმენით ლისტი და დაამატეთ მხოლოდ კენტი რიცხვები ახალ ლისტში
odd_list = [num for num in numbers if num % 2 != 0]
print("ახალი კენტი რიცხვების ლისტი:", odd_list)

# ცარიელი სიის შექმნა
user_numbers = []

# 5 რიცხვის შეყვანა მომხმარებლისგან
for i in range(5):
    number = int(input(f"შეიყვანეთ {i+1}-ე რიცხვი: "))
    user_numbers.append(number)

# სიის დაბეჭდვა
print("თქვენი შეყვანილი რიცხვების სია:", user_numbers)

# რიცხვების სია 1-10 ჩათვლით
numbers = list(range(1, 11))

# while ციკლი სიიდან ყველა ელემენტის წასაშლელად
while numbers:
    # pop იღებს ბოლო ელემენტს სიიდან და ამავდროულად შლის მას
    removed_number = numbers.pop()
    print(f"წაშლილი რიცხვი: {removed_number}")

print("სიიდან ყველა ელემენტი წაშლილია.")
# ცარიელი shopping სია
shopping_list = []

print("მოგესალმებით შოპინგ სიაში! შეგიძლიათ დაამატოთ ან წაშალოთ პროდუქტი. მორჩენისას აკრიფეთ 'done'.\n")

while True:
    action = input("შეიყვანეთ 'add' დასამატებლად, 'remove' წასაშლელად, ან 'done' დასრულებისთვის: ").lower()

    if action == 'add':
        product = input("რა გსურთ დაამატოთ?: ")
        shopping_list.append(product)
        print(f"პროდუქტი '{product}' დაემატა სიაში.")
    elif action == 'remove':
        product = input("რა გსურთ წაშალოთ?: ")
        if product in shopping_list:
            shopping_list.remove(product)
            print(f"პროდუქტი '{product}' წაიშალა სიიდან.")
        else:
            print(f"პროდუქტი '{product}' სიაში არ არის.")
    elif action == 'done':
        break
    else:
        print("არასწორი ქმედება. სცადეთ თავიდან.")

# საბოლოო სიის დაბეჭდვა
print("\nთქვენი საბოლოო შოპინგ სია:")
for item in shopping_list:
    print(f"- {item}")


# თავდაპირველი სია
numbers = [1, 2, 3, 4, 5]

# ახალი სიის შექმნა
reversed_numbers = []

# არსებული სიის შებრუნება append და pop გამოყენებით
while numbers:
    reversed_numbers.append(numbers.pop())

# დაბეჭდვა
print("შებრუნებული სია:", reversed_numbers)
