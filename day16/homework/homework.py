# მომხმარებლის სახელის შეყვანა
user_name = input("ჯეკო: ")

# ჩემი სახელი
my_name = "ჯეკო"

# შედარება
if user_name == my_name:
    print("ერთნაირი სახელები გვაქვს!")
else:
    print("სასიამოვნოა თქვენი გაცნობა!")

# ასაკის შეყვანა
age = int(input("19:"))

# 17 წელს ქვემოთ მართვის მოწმობის აღება შეუძლებელია
if age >= 17:
    print("მე 19 წლის ვარ აიმტომ შემიძლია მართვის მოწმობის აღება")

# ჩემი ასაკი
my_age = 19

# მომხმარებლის ასაკი
user_age = int(input("19: "))

if my_age > user_age:
    print("ტოლებნები.")
elif my_age < user_age:
    print("ტოლებნები.")
else:
    print("ჩვენ ტოლები ვართ")


    # მომხმარებლის სიმაღლე და წონა
height = int(input("1.80): "))
weight = int(input("70): "))

# ზოოპარკში შესვლის წესი
if height >= 180 and 50 <= weight <= 90:
    print("თქვენ შეგიძლიათ იმგზავროთ ზოოპარკში!")


# მომხმარებლის წონა
weight = int(input("შეიყვანეთ თქვენი წონა (კილოგრამებში): "))

# წამლის დოზა
if 10 <= weight <= 20:
    print(" უნდა დალიო ნახევარი ტაბლეტი დღეში.")
elif 30 <= weight <= 40:
    print(" 1 ტაბლეტი ორჯერ დღეში.")
elif weight > 45:
    print(" 3 ტაბლეტი ორჯერ დღეში.")
else:
    print("70.")


    # მაღაზიაში მინერალური წყლის 
has_mineral_water = input("მაღაზიაში არის მინერალური წყალი")

if has_mineral_water == "True":
    print("მაღაზიაში მინერალური წყალი აქვთ.")


