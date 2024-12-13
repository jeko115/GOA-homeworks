number = int(input("50: "))
if number % 3 == 0:
    print(f"{number} არის სამის ჯერადი.")
else:
    print(f"{number} არ არის სამის ჯერადი.")


number = int(input("50: "))
if number % 5 == 0:
    print(f"{number} არის ხუთის ჯერადი.")
else:
    print(f"{number} არ არის ხუთის ჯერადი.")



number = int(input("50: "))
if number > 0:
    print(f"{number} არის დადებითი.")
elif number < 0:
    print(f"{number} არის უარყოფითი.")
else:
    print("რიცხვი არის ნული.")


for i in range(0, 51, 2):
    print(i)


for i in range(1, 31, 2):
    print(i)


for i in range(71):
    if i % 2 == 0:
        print(f"{i} - ლუწია")
    else:
        print(f"{i} - კენტია")



for i in range(0, 101, 5):
    print(i)


for i in range(0, 51, 3):
    print(i)


number = int(input("50: "))
for i in range(number + 1):
    print(i)

    number = int(input("50: "))
for i in range(number + 1):
    if i % 2 == 0:
        print(i)


number = int(input("50: "))
for i in range(number + 1):
    if i % 2 != 0:
        print(i)


number = int(input("50: "))
for i in range(number + 1):
    if i % 2 == 0:
        print(f"{i} - ლუწია")
    else:
        print(f"{i} - კენტია")


number = int(input("50: "))
for i in range(0, number + 1, 5):
    print(i)

