def greet():
    print("გამარჯობა!")

def greet_user():
    name = input("შეიყვანეთ თქვენი სახელი: ")
    print(f"გამარჯობა, {name}!")

def add_numbers():
    a = float(input("შეიყვანეთ პირველი რიცხვი: "))
    b = float(input("შეიყვანეთ მეორე რიცხვი: "))
    print(f"ჯამი: {a + b}")

def subtract_numbers():
    a = float(input("შეიყვანეთ პირველი რიცხვი: "))
    b = float(input("შეიყვანეთ მეორე რიცხვი: "))
    print(f"სხვაობა: {a - b}")

def multiply_numbers():
    a = float(input("შეიყვანეთ პირველი რიცხვი: "))
    b = float(input("შეიყვანეთ მეორე რიცხვი: "))
    print(f"ნამრავლი: {a * b}")

def divide_numbers():
    a = float(input("შეიყვანეთ პირველი რიცხვი: "))
    b = float(input("შეიყვანეთ მეორე რიცხვი: "))
    if b != 0:
        print(f"გაყოფის შედეგი: {a / b}")
    else:
        print("ნულზე გაყოფა შეუძლებელია!")

def check_even_odd():
    num = int(input("შეიყვანეთ რიცხვი: "))
    if num % 2 == 0:
        print("ლუწი")
    else:
        print("კენტი")

def check_positive_negative():
    num = float(input("შეიყვანეთ რიცხვი: "))
    if num > 0:
        print("დადებითი")
    elif num < 0:
        print("უარყოფითი")
    else:
        print("ნულია")

def check_adulthood():
    age = int(input("შეიყვანეთ ასაკი: "))
    if age >= 18:
        print("თქვენ სრულწლოვანი ხართ")
    else:
        print("თქვენ არ ხართ სრულწლოვანი")

def print_numbers():
    num = int(input("შეიყვანეთ რიცხვი: "))
    for i in range(1, num + 1):
        print(i)

def print_even_numbers():
    num = int(input("შეიყვანეთ რიცხვი: "))
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i)

def print_odd_numbers():
    num = int(input("შეიყვანეთ რიცხვი: "))
    for i in range(1, num + 1):
        if i % 2 != 0:
            print(i)

def sum_list():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"სიაში არსებული რიცხვების ჯამი: {sum(numbers)}")
