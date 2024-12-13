i = 10
while i >= 1:
    print(i)
    i -= 1


for i in range(1, 21):
    if i != 5 and i != 15:
        print(i)



word = input("GOA: ")
for letter in word:
    print(letter)



for i in range(1, 11):
    if i % 2 == 0:
        print("მე მიყვარს გოა")  # ლუწი რიცხვებისთვის
    else:
        print("მე მიყვარს პროგრამირება")  # კენტი რიცხვებისთვის



for i in range(1, 31):
    if i % 2 == 0:
        print(f"{i} - ლუწია")
    else:
        print(f"{i} - კენტია")


for i in range(1, 31):
    if i % 2 == 0:
        print(f"{i} - ლუწია")
    else:
        print(f"{i} - კენტია")



for i in range(10, 0, -1):
    print(i)
