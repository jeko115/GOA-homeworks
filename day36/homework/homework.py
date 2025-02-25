def greet_user(name):
    print(f"გამარჯობა, {name}!")


def sum_numbers(a, b):
    print(f"ჯამი: {a + b}")


def divide_numbers(a, b):
    if b != 0:
        print(f"განაყოფი: {a / b}")
    else:
        print("ნულზე გაყოფა შეუძლებელია!")


def multiply_numbers(a, b):
    print(f"ნამრავლი: {a * b}")


def check_even_odd(num):
    if num % 2 == 0:
        print("რიცხვი ლუწია")
    else:
        print("რიცხვი კენტია")


def check_positive_negative(num):
    if num > 0:
        print("რიცხვი დადებითია")
    elif num < 0:
        print("რიცხვი უარყოფითია")
    else:
        print("რიცხვი ნულია")


def check_adulthood(age):
    if age >= 18:
        print("სრულწლოვანი ხარ")
    else:
        print("არ ხარ სრულწლოვანი")


def print_numbers_up_to(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()


def print_even_numbers_up_to(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print()


def print_odd_numbers_up_to(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()


# მომხმარებლის შეყვანის მოთხოვნა
name = input("შეიყვანეთ თქვენი სახელი: ")
greet_user(name)

a = int(input("შეიყვანეთ პირველი რიცხვი: "))
b = int(input("შეიყვანეთ მეორე რიცხვი: "))

sum_numbers(a, b)
divide_numbers(a, b)
multiply_numbers(a, b)

num = int(input("შეიყვანეთ რიცხვი: "))
check_even_odd(num)
check_positive_negative(num)
check_adulthood(num)
print_numbers_up_to(num)
print_even_numbers_up_to(num)
print_odd_numbers_up_to(num)
